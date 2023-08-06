from __future__ import print_function
import sys
import os
import logging
import json
import copy
from os.path import dirname
from jsonschema import validate
import importlib
import pkgutil
import tempfile
import uuid
from halocli.exception import HaloPluginException
from halocli.util import Util

logger = logging.getLogger(__name__)

logging.root.setLevel(logging.INFO)

"""
the bian lite plugin
---------------

1. rename bian swagger files to _lite suffix : 

2. add "LITE" marker to swagger info block: "revision":"lite"

3. detect service domain name from info/title block (sd_name) : CurrentAccount

4. detect functional pattern name from config file or command line or from swagger file (fp_name) : FulfillmentArrangement

GENERAL:

5. remove all sd session methods with end with : activation,configuration,feedback

6. remove from all url the section containing sd-reference-id and the sd_name+fp_name ->  "{sd-reference-id}/current-account-fulfillment-arrangement/":
   this -> "/current-account/{sd-reference-id}/current-account-fulfillment-arrangement/{cr-reference-id}/issueddevice/{bq-reference-id}/update"
   becomes this -> "/current-account/{cr-ref-id}/issueddevice/{bq-ref-id}/update"
   the url is build with "/"+sd_name+"/{cr-ref-id}/"+bq_name+"/{bq-ref-id}/"+action_name
   
7. remove field sd_name+ServicingSessionReference : "currentAccountServicingSessionReference" from all return blocks

8. remove sd_name+fp_name : currentAccountFulfillmentArrangement in all response blocks field names and also in the definition models if relevant

9. remove all definitions which are not referenced in the swagger

RETRIEVE:

10. remove reporting block from each retrieve method return block - (sd+fp)InstanceReportRecord or (sd+fp)InstanceReport : currentAccountFulfillmentArrangementInstanceReportRecord

11. remove analysis block from each retrieve method return block - (sd+fp)InstanceAnalysis : currentAccountFulfillmentArrangementInstanceAnalysis

12. remove analysis block from each retrieve method return block - (sd+fp)RetrieveActionResponse : currentAccountFulfillmentArrangementRetrieveActionResponse


"""

class Plugin():

    def __init__(self,halo):
        #init vars
        self.halo = halo

        #init work on halo config
        #if self.halo.config ...

        self.name = 'lite'
        self.desc = 'lite version of bian swagger file'

        # set commands
        self.commands = {
            'create': {
                'usage': "Create a lite bian swagger file",
                'lifecycleEvents': ['generate', 'write'],
                'options': {
                    'destination': {
                        'usage': 'Path of the destination dir',
                        'shortcut': 'd',
                        'required': True
                    },
                    'path': {
                        'usage': 'Path of the source swagger file dir',
                        'shortcut': 'p',
                        'required': True
                    },
                    'file': {
                        'usage': 'add swagger file',
                        'shortcut': 'f'
                    },
                    'all': {
                        'usage': 'run all options',
                        'shortcut': 'a'
                    }
                }
            }
        }

        # set hooks
        self.hooks = {
            'before:create:generate': self.before_swagger_generate,
            'create:generate': self.swagger_generate,
            'after:create:generate': self.after_swagger_generate,
            'create:write': self.swagger_write
        }

        #logger.info('finished plugin')

    def run_plugin(self,options):
        self.options = options
        #do more

    def fix_props(self,props,sdfp):
        propsx = copy.deepcopy(props)
        for name in propsx:
            if name.endswith("ServicingSessionReference"):
                del props[name]
                continue
            if name.endswith("InstanceReportRecord") or name.endswith("InstanceReport"):
                del props[name]
                continue
            if name.endswith("InstanceAnalysis"):
                del props[name]
                continue
            if name.endswith("RetrieveActionResponse"):
                del props[name]
                continue
            if name.startswith(sdfp):
                props[name.replace(sdfp, "")] = propsx[name]
                del props[name]
                continue

    def get_sdfph(self,data):
        #/current-account/{sd-reference-id}/current-account-fulfillment-arrangement/{cr-reference-id}
        for d in data['paths']:
            if d.endswith("/{cr-reference-id}"):
                j = d.index("/{cr-reference-id}")
                i = d.index("/{sd-reference-id}")
                return d[i+18:j]

    def get_sdfp(self,data):
        #return self.get_sdfph(data).replace("-","").replace("/","")
        s = self.get_sdfph(data)
        while "-" in s:
            i = s.index("-")
            s = s[:i] + s[i+1].swapcase() + s[i+2:]
        return s.replace("/","")

    def before_swagger_generate(self):
        for o in self.options:
            if 'destination' in o:
                self.destination = o['destination']
            if 'path' in o:
                self.path = o['path']
            if 'all' in o:
                self.all = o['all']
            if 'file' in o:
                self.swagger_source = o['file']
        if not self.destination:
            raise Exception("no destination found")
        if self.swagger_source:
            urls = os.path.join(self.path, self.swagger_source)
        else:
            urls = os.path.join('.', self.swagger_source)#self.halo.settings['mservices'][self.service]['record']['path']
        try:
            self.data = Util.analyze_swagger(urls)
        except Exception as e:
            self.halo.cli.error("error in source swagger file validation:"+self.swagger_source+"->"+str(e))
            raise e

    def swagger_generate(self):
        data = self.data
        sdfph = self.get_sdfph(data)#"/current-account-fulfillment-arrangement"
        self.halo.cli.log("sdfph:" + sdfph)
        sdfp = self.get_sdfp(data)#"currentAccountFulfillmentArrangement"
        self.halo.cli.log("sdfp:" + sdfp)
        tmp = {}
        data["info"]["title"] = data["info"]["title"]+"(Lite)"
        for d in data['paths']:
            m = data['paths'][d]
            new_m = copy.deepcopy(m)
            tmp[d] = new_m
        if self.all:
            for k in tmp:
                new_m = tmp[k]
                path = k
                if path.endswith("/activation") or path.endswith("/configuration") or path.endswith("/feedback"):
                    del data['paths'][k]
                    continue
                if path.find("/{sd-reference-id}") >= 0:
                    del data['paths'][k]
                    path = path.replace("/{sd-reference-id}","").replace("-reference-","-ref-")
                if path.find(sdfph) >= 0:
                    if k in data['paths']:
                        del data['paths'][k]
                    occr = path.rfind(sdfph)
                    if occr > 0:
                        path = path[:occr]+path[occr:].replace(sdfph,"")
                for o in new_m:# get,put,post,delete
                    self.halo.cli.log("path:" + path+" op:"+o)
                    rem_p = None
                    for p in new_m[o]['parameters']:
                        self.halo.cli.log(path+":"+p['name'])
                        if p['name'].find("sd-reference-id") >= 0:
                            rem_p = p
                            continue
                        if p['name'].find("-reference-") >= 0:
                            p['name'] = p['name'].replace("-reference-","-ref-")
                        if p['name'].find("body") >= 0:
                            props = p['schema']['properties']
                            self.fix_props(props, sdfp)
                    if rem_p:
                        new_m[o]['parameters'].remove(rem_p)
                    if '200' in new_m[o]['responses']:
                        if 'items' in new_m[o]['responses']['200']['schema']:
                            if 'properties' in new_m[o]['responses']['200']['schema']['items']:
                                props = new_m[o]['responses']['200']['schema']['items']['properties']
                            else:
                                props = new_m[o]['responses']['200']['schema']['items']
                        else:
                            props = new_m[o]['responses']['200']['schema']['properties']
                    else:
                        if 'items' in new_m[o]['responses']['201']['schema']:
                            props = new_m[o]['responses']['201']['schema']['items']['properties']
                        else:
                            props = new_m[o]['responses']['201']['schema']['properties']
                    self.fix_props(props,sdfp)
                data['paths'][path] = new_m
        del data['definitions']
        data['definitions'] = {}
        self.halo.cli.log("finished extend successfully")


    def after_swagger_generate(self):
        data = self.data
        try:
            Util.validate_swagger(data)
        except Exception as e:
            self.halo.cli.error("error in generated swagger file validation:"+self.swagger_source+"->"+str(e))
            raise e

    def swagger_write(self):
        self.file_write()

    def file_write(self):
        try:
            path = self.destination
            if path:
                file_path = os.path.join(path, str(self.swagger_source.replace(".json","_lite.json")))
            else:
                dir_tmp = tempfile.TemporaryDirectory()
                file_path = os.path.join(dir_tmp.name, str(uuid.uuid4()) + "_lite.json")
            logger.debug(file_path)
            f = open(file_path, "w")
            f.write("")
            f.close()
            Util.dump_file(file_path, self.data)
            logging.debug("Swagger file generated:" + file_path)
            """
            with open(file_path, 'r') as fi:
                f = fi.read()
                print(str(f))
                return f
            """
        except Exception as e:
            raise HaloPluginException(str(e))

