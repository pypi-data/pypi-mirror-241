"""System module."""
from __future__ import absolute_import
import sys
import os
import json
import collections
from pathlib import Path
import base64
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from PIL import Image


class TypeDir:
    ''' Type Dir '''
    PROJECT_MAIN_DIR = 0
    PROJECT_DIR = 1
    IDCYCLE_DIR = 2
    STEP_DIR = 3
    CONFIGURATIONSTEP_DIR = 4
    PLUGIN_DIR = 5
    ENVIRONMENTS_DIR = 6


class Connection:
    ''' Connection '''
    @staticmethod
    def start(method, url, payload=None, api_key=None, debug=False):
        ''' start '''
        req = None
        headers = {"Content-Type": "application/json", "Idelium-Key": api_key}
        if method == "POST":
            req = requests.post(url,
                              headers=headers,
                              data=json.dumps(payload),
                              verify=False)
        elif method == "PUT":
            req = requests.put(url,
                             headers=headers,
                             data=json.dumps(payload),
                             verify=False)
        elif method == "GET":
            req = requests.get(url, headers=headers, verify=False)
        if debug is True:
            print("Response: " + req.text)
            print("Headers: " + json.dumps(headers))
            print("Payload: " + json.dumps(payload))
            print(str(req.status_code) + " " + method + " " + url)
        return json.loads(req.text, object_pairs_hook=collections.OrderedDict)


class IdeliumWs:
    ''' IdeliumWs'''
    @staticmethod
    def create_folder(config):
        ''' create folder '''
        url = config["api_idelium"] + "testcycle"
        payload = {
            "testCycleId": config['idCycle'],
        }
        return Connection.start("POST", url, payload, config["ideliumKey"],
                                config["is_debug"])

    @staticmethod
    def create_test(config, id_test, name):
        ''' create test '''
        url = config["api_idelium"] + "test"
        payload = {
            "testCycleId": config['idCycle'],
            "testId": id_test,
            "name": name,
        }
        return Connection.start("POST", url, payload, config["ideliumKey"],
                                config["is_debug"])

    @staticmethod
    def update_test(config, id_test, status,postman_data):
        ''' create test '''
        url = config["api_idelium"] + "test"
        payload = {
            "testId": id_test,
            "status": status,
            "postmanData" : postman_data,
        }
        return Connection.start("PUT", url, payload, config["ideliumKey"],
                                config["is_debug"])

    @staticmethod
    def create_step(config, id_test, id_step, name, status, data, typeofstep):
        ''' create step '''
        url = config["api_idelium"] + "step"
        payload = {
            "testCycleId": config['idCycle'],
            "testId": id_test,
            "stepId": id_step,
            "name": name,
            "status": int(status),
            "data": json.dumps(data),
            "type": typeofstep,
            "screenshots": "[]",
        }
        return Connection.start("POST", url, payload, config["ideliumKey"],
                                config["is_debug"])

    @staticmethod
    def update_step(config, id_step, screenshots):
        ''' update step '''
        url = config["api_idelium"] + "step"
        payload = {
            "stepId": id_step,
            "screenshots": json.dumps(screenshots),
        }
        return Connection.start("PUT", url, payload, config["ideliumKey"],
                                config["is_debug"])

    @staticmethod
    def get_environments(config):
        ''' get environment '''
        url = config["api_idelium"] + "environments/" + str(
            config["idProject"])
        return Connection.start("GET", url, None, config["ideliumKey"],
                                config["is_debug"])

    @staticmethod
    def get_cycles(config):
        ''' get cycles '''
        url = config["api_idelium"] + "testcycle/" + config['idCycle']
        json_cycle = Connection.start("GET", url, None, config["ideliumKey"],
                                     config["is_debug"])
        if "config" in json_cycle:
            return json.loads(json_cycle["config"])
        return -1

    @staticmethod
    def get_tests(config, id_test):
        ''' get tests '''
        url = config["api_idelium"] + "test/" + str(id_test)
        json_test = Connection.start("GET", url, None, config["ideliumKey"],
                                    config["is_debug"])
        return json.loads(json_test["config"])

    @staticmethod
    def get_step(config, id_step):
        ''' get step '''
        url = config["api_idelium"] + "step/" + str(id_step)
        json_step = Connection.start("GET", url, None, config["ideliumKey"],
                                    config["is_debug"])
        return {
            "objectStep": json.loads(json_step["config"]),
            "step_json_name": json_step["name"] + "_" + str(id_step),
            "step_json_description": json_step["name"],
        }
    @staticmethod
    def create_directories(config):
        ''' create directories '''
        configuration_directories = [
            config["dir_idelium_scripts"],
            config["dir_idelium_scripts"] + "/" + config["idProject"],
            config["dir_idelium_scripts"] + "/" + config["idProject"] + "/" +
            config['idCycle'],
            config["dir_idelium_scripts"] + "/" + config["idProject"] + "/" +
            config['idCycle'] + "/step",
            config["dir_idelium_scripts"] + "/" + config["idProject"] + "/" +
            config['idCycle'] + "/configurationStep",
            config["dir_idelium_scripts"] + "/" + config["idProject"] + "/" +
            config['idCycle'] + "/plugin",
            config["dir_idelium_scripts"] + "/" + config["idProject"] + "/" +
            config['idCycle'] + "/environments",
        ]
        print("start download configuration")
        return configuration_directories

    def get_configuration (self, config):
        ''' download configuration files '''
        printer = config["printer"]
        configuration_step = {}
        configuration_directories = self.create_directories(config)
        object_cycle = self.get_cycles(config)
        if object_cycle == -1:
            printer.danger("The id_cycle " + str(config["idCycle"]) +
                           " not exist")
            if config['ideliumServer'] is False:
                sys.exit(1)
            else:
                return False
        array_steps = {}
        array_environments = {}
        array_plugins = {}
        config_step = None
        #search cycle for this cycle
        for cycle in object_cycle:
            object_test = self.get_tests(config, cycle["id"])
            for test in object_test:
                step = self.get_step(config, test["id"])
                # write step
                array_steps[step["step_json_name"]] = step["objectStep"]
                print(step["step_json_name"])
                json_file_path = (configuration_directories[TypeDir.STEP_DIR] +
                                "/" + step["step_json_name"] + ".json")
                if config["local"] is True and (
                        Path(json_file_path).exists() is False
                        or config["forcedownload"] is True):
                    with open(json_file_path, "w") as file:
                        json.dump(step["objectStep"],
                                  file,
                                  indent=4,
                                  sort_keys=False)
        #write_configuration_step
        config_step = None
        json_file_path = (
            configuration_directories[TypeDir.CONFIGURATIONSTEP_DIR] +
            "/config_step.json")
        if config["local"] is True and (Path(json_file_path).exists() is False
                                        or config["forcedownload"] is True):
            with open(json_file_path, "w") as file:
                json.dump(configuration_step, file, indent=4, sort_keys=False)
        #search  plugins for projectId
        url = config["api_idelium"] + "plugins/" + str(config["idProject"])
        json_plugins = Connection.start("GET", url, None, config["ideliumKey"],
                                       config["is_debug"])
        for plugin_det in json_plugins:
            url = config["api_idelium"] + "plugin/" + str(plugin_det["id"])
            json_plugin = Connection.start("GET", url, None,
                                          config["ideliumKey"],
                                          config["is_debug"])
            #save  plugin for projectId
            json_plugin_code=json.loads(json_plugin['code'])
            array_plugins[json_plugin["name"]] = json_plugin["code"]
            plugins_dir = config["dir_idelium_scripts"] + "/" +  config["idProject"] + "/plugin"
            py_file_path=(plugins_dir + "/" +
                          json_plugin["name"] + ".py")
            if Path(plugins_dir).exists() is False:
                os.makedirs(plugins_dir)
                if config["is_debug"] is True:
                    print("created temporary directory", plugins_dir)
            if config["is_debug"] is True:
                print("plugin file saved in:", py_file_path)
            py_file = open(py_file_path, "wt")
            py_file.write(json_plugin_code[0])
            py_file.close()
        #download environments
        json_environments = self.get_environments(config)
        printer.success("finish download file")
        for env in json_environments:
            url = config["api_idelium"] + "environment/" + str(env["id"])
            json_environment = Connection.start("GET", url, None,
                                               config["ideliumKey"],
                                               config["is_debug"])
            file_name_env = json_environment["code"]
            code_environment = json.loads(
                json_environment["config"],
                object_pairs_hook=collections.OrderedDict)
            array_environments[file_name_env] = code_environment
            json_file_path = (
                configuration_directories[TypeDir.ENVIRONMENTS_DIR] + "/" +
                file_name_env + ".json")
            if config["local"] is True and (
                    Path(json_file_path).exists() is False
                    or config["forcedownload"] is True):
                with open(json_file_path, "w") as file:
                    json.dump(code_environment, file, indent=4, sort_keys=False)
        return {
            "steps":
            array_steps,
            "environments":
            array_environments,
            "plugins":
            array_plugins,
            "configStep":
            config_step,
            "environmentDir":
            configuration_directories[TypeDir.ENVIRONMENTS_DIR],
            "stepDir":
            configuration_directories[TypeDir.STEP_DIR],
            "config_stepDir":
            configuration_directories[TypeDir.CONFIGURATIONSTEP_DIR],
            "id_cycleDir":
            configuration_directories[TypeDir.IDCYCLE_DIR],
        }

    def start_test(self, idelium, test_configurations, config):
        ''' start test '''
        if config['ideliumServer'] is True:
            Path(config['dir_idelium_scripts'] + 'server').touch()
        wrapper = idelium.get_wrapper(config)
        object_cycle = self.get_cycles(config)
        driver = None
        id_cycle = self.create_folder(config)['idCycle']
        for cycle in object_cycle:
            #search test for this cycle
            printer = config["printer"]
            object_test = self.get_tests(config, cycle["id"])
            printer.success("Test: " + cycle["description"])
            id_test = self.create_test(config, id_cycle, cycle["name"])['idTest']
            test_failed = False
            for test in object_test:
                if test_failed is False:
                    json_step = test_configurations["steps"][test["name"] +
                                                            "_" +
                                                            str(test["id"])]
                    printer.underline(json_step["name"] + "(" +
                                      str(test["id"]) + ")")
                    config["wrapper"] = wrapper
                    config["printer"] = printer
                    config["json_step"] = json_step
                    object_return = idelium.execute_step(driver, config)
                    status = object_return["status"]
                    driver = object_return["driver"]
                    postman_data=object_return["postman_data"]
                    typeofstep=object_return["type"]
                    step_failed = object_return["step_failed"]
                    config["status"] = status
                    config["step_failed"] = step_failed
                    id_step = None
                    #test["name"],
                    if config["test"] is False:
                        id_step = self.create_step(config, id_test, test["id"],
                                                 json_step["name"],
                                                 status,
                                                 postman_data,
                                                 typeofstep
                                                 )['idStep']
                    if status in ('2','5') and object_return['type']=='seleniumOrAppium':
                        path = "screenshots/"
                        file_name = str(id_test) + ".png"
                        if not os.path.exists(path):
                            os.makedirs(path)
                        if config["json_step"]["attachScreenshot"] is True:
                            wrapper.screen_shot(driver, path + file_name,config['ideliumServer'])
                        if config["test"] is False:
                            file_name_jpg = path + str(id_test) + ".jpg"
                            with Image.open(path + file_name) as img:
                                rgb_im = img.convert("RGB")
                                rgb_im.save(file_name_jpg)
                                with open(file_name_jpg, "rb") as img_file:
                                    screenshot_base64 = base64.b64encode(
                                        img_file.read())
                                    self.update_step(
                                        config,
                                        id_step,
                                        [
                                            "data:image/jpg;base64," +
                                            str(screenshot_base64)[2:-1]
                                        ],
                                    )

                            os.unlink(path + file_name)
                            os.unlink(file_name_jpg)
                        if config["json_step"]["failedExit"] is True:
                            printer.danger(
                            "The test '" + cycle["name"] +
                            "' it is forcibly interrupted due to the blocking failure of the step"
                            )
                            id_test = self.update_test(config, id_test, 2, postman_data)
                            test_failed = True
                    else:
                        self.update_test(config, id_test, 1, postman_data)
            if config['ideliumServer'] is True:
                os.remove(config['dir_idelium_scripts'] + 'server')
            if driver != None:
                driver.quit()
