"""System module."""
from __future__ import absolute_import
import sys
import tempfile
from pathlib import Path
import selenium


class InitIdelium():
    ''' init '''
    @staticmethod
    def get_selenium_version():
        ''' version selenium '''
        return selenium.__version__

    @staticmethod
    def get_syntax():
        ''' help command line '''
        return """
    \033[1mUsage\033[0m: idelium [options]

    Options:

    --help                  show this help
    --idCycle               cycle id to associate to the execution "idCycle1,idCycle2,...."
    --idProject             force idProject
    --environment           environment json config file (required)
    --useragent             set useragent for the test
    --test                  for testing without store the results
    --verbose               for debugging 
    --dirChromedriver       default path of chromedriver path ("./chromedriver/last")
    --dirConfigurationStep  default path ("./configurationStep") for configuration steps 
    --dirStepFiles          default path ("./step") of directory for step files 
    --dirIdeliumScript      default path (".") of directory for step files
    --width                 default width of screen 1024
    --height                default height of screen 768
    --device                if is set useragent,height and width are ignored
    --url                   url for test 
    --ideliumwsBaseurl      idelium server url ex: https://localhost
    --reportingService      where the data will be save: idelium | zephyr
    --ideliumKey            is the key for access to the idelium api
    --idChannel             idChannel
    
    Idelium server
    --ideliumServer         with this option idelium-cli is in server mode
    --ideliumServerPort     default is 8691

    Zephir 
    --jiraApiUrl            for change the default jira url (https://<host jira>/rest/api/latest/)
    --idJira                jira id (required if idVersion and idCycle not setted)
    --idVersion             version id to associate the execution 
    --username              jira username (required)
    --password              jira password (required)



    For Example: 

    default reporting service: idelium --ideliumKey=1234 --idCycle=2 --idProject=8 --environment=prod

    working with jira/zephyr: idelium --reportingService=zephyr --idJira=prj-1234 --username=user --password=secret --environment=prod.json --useragent='apple 1134'

    """
    @staticmethod
    def get_reguired_parameters():
        """Returns a dictionary of the required parameters for Idelium."""
        return {
            "idProject" : 0,
            "idCycle" : 0,
            "environment" : 0,
            "ideliumKey": 0,
        }
    @staticmethod
    def get_default_parameters():
        """Returns a dictionary of the default parameters for Idelium."""
        return {
            'execution_name': 'automation test python',
            'reportingService': 'idelium',
            'ideliumwsBaseurl': 'https://service.idelium.io',
            'base_url':None,
            'zephyrApiUrl':None,
            'jiraApiUrl':None,
            'dir_plugins':"plugin",
            'test':False,
            'is_debug':False,
            'device':None,
            'width': 1920,
            'height':1080,
            'username':None,
            'password':None,
            'environment':None,
            'idJira':None,
            'fileSteps':None,
            'idVersion':None,
            'idCycle':None,
            'useragent':None,
            'idProject':None,
            'idChannel' : None,
            'url' : None,
            'isRealDevice' : False,
            'os' : None,
            'appiumServer' : None,
            'appiumDesiredCaps' : None,
            'count':0,
            'ideliumKey':None,
            'forcedownload':False,
            'local':False,
            'ideliumServer': False,
            'ideliumServerPort': 8691,
        }
    def define_parameters(self,args,ideliumws,printer):
        ''' set all necessary parameters '''
        cl_params= self.get_default_parameters()
        check_required=self.get_reguired_parameters()
        cl_params['dir_idelium_scripts'] = tempfile.mkdtemp()
        count=0
        for i in args:
            array_command=i.split("=")
            command=array_command[0][2:]
            if command in cl_params:
                if command == 'ideliumKey':
                    cl_params['ideliumKey']=''
                    if len(array_command)==3:
                        cl_params['ideliumKey'] = array_command[1] + '=' 
                    else:
                        cl_params['ideliumKey'] = array_command[1]
                elif command == "forcedownload":                
                    cl_params['forcedownload'] = True
                elif command == 'ideliumServer':
                    cl_params['ideliumServer'] = True
                elif command == 'ideliumServerPort': 
                    cl_params['ideliumServerPort'] = int(array_command[1])
                else:
                    cl_params[command]=array_command[1]
                if command in check_required:
                    check_required[command]=1
            elif array_command[0] == "--verbose":
                cl_params['is_debug'] = True
            elif array_command[0] == "--help":
                print(self.get_syntax())
                sys.exit(0)
            else:
                if count > 0:
                    print (self.get_syntax())
                    print("\n" + array_command[0] + ": is not a valid option")
                    sys.exit(1)
            count += 1
        count_req=0
        for i in check_required:
            count_req=count_req + check_required[i]
        if cl_params['ideliumServer'] is False:
            if cl_params['ideliumKey']is None:
                file_idelium_key=str(Path.home()) + '/.idelium'
                if Path(file_idelium_key).is_file() is True:
                    file = open(file_idelium_key, "r")
                    cl_params['ideliumKey']=file.read()
                else:
                    print (self.get_syntax())
                    printer.danger('ideliumKey is not setted !')
                    sys.exit(1)
        if cl_params['ideliumServer'] is False:
            if cl_params['reportingService'] == 'idelium':
                if (cl_params['idProject'] is None
                        or cl_params['idCycle'] is None):
                    print(self.get_syntax())
                    printer.danger("\nidProject and idCycle are mandatory")
                    sys.exit(1)
                if cl_params['reportingService'] == 'zephyr':
                    if count_req < 4:
                        print(self.get_syntax())
                        printer.danger("\nMissed required options")
                        sys.exit(1)
                if cl_params['environment'] is None:
                    print(self.get_syntax())
                    printer.danger("\nenvironment must be set")
                    sys.exit(1)
        return {
            'cl_params': cl_params,
        }

    def load_parameters(self, cl_params, ideliumws, printer):

        sys.path.append(cl_params['dir_idelium_scripts'] + "/" + cl_params['idProject'])

        cl_params['api_idelium']=cl_params['ideliumwsBaseurl'] + '/api/ideliumcl/'
        cl_params['printer']=printer
        test_config=None
        json_config=None
        json_step_config=None
        test_config = ideliumws.get_configuration(cl_params)
        if test_config is False:
            return False
        print('Environment:' + cl_params['environment'])
        if cl_params['environment'] in test_config['environments']:
            json_config=test_config['environments'][cl_params['environment']]
        else:
            printer.danger('Environment "' + cl_params['environment']
                            + '" or idProject ' + cl_params['idProject'] + ' not exist')
            sys.exit(1)
        if 'userAgent' in json_config:
            cl_params['user_agent']=json_config['userAgent']
        if 'isRealDevice' in json_config:
            cl_params['isRealDevice']=json_config['isRealDevice']
        if 'appiumServer' in json_config:
            cl_params['appiumServer']=json_config['appiumServer']
        if 'isRealDevice' in json_config:
            cl_params['appiumDesiredCaps']=json_config['appiumDesiredCaps']
        if cl_params['idProject'] is not None:
            json_config['projectId'] = cl_params['idProject']

        json_step_config=test_config['configStep']
        if cl_params['idProject'] is not None and json_step_config is not None:
            json_step_config['idProject']=cl_params['idProject']
        if 'device' in json_config:
            cl_params['device'] = json_config['device']
        if cl_params['url'] is not None:
            json_config['url']=cl_params['url']
        cl_params['json_config']=json_config
        cl_params['json_step_config']=json_step_config

        return {
            'cl_params': cl_params,
            'test_config': test_config
        }