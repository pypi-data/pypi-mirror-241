from typing import List
import os,sys
from pnostic.structure import RepoObject, RepoResultObject, SeclusionEnv, SeclusionEnvOutput, Runner


class app(SeclusionEnv):
    def __init__(self, working_dir:str, docker_image:str, docker_name:str):
        super().__init__(working_dir=working_dir)
        self.imports = [
            "sdock[all]"
        ]
        self.docker_image = docker_image
        self.total_imports = []
        self.total_files = []
        self.docker_name = docker_name

    def initialize(self) -> bool:
        return True

    def name(self) -> str:
        return "TitanSeclusion"

    @property
    def runner_file_name(self):
        return "seclusion_env_{0}_input.py".format(self.name())

    @property
    def runner_file_name_output(self):
        return "seclusion_env_{0}_output.zip".format(self.name())

    def clean(self) -> bool:
        return True

    def python_packages(self,packages:List[str]) -> bool:
        self.total_imports.extend(packages)
        return True

    def setup_files(self,files:List[str]) -> bool:
        self.total_files.extend(files)
        return True

    def __py_script_contents(self, runner, path_to_scan):
        return f"""#!/usr/bin/env python3
import sys,os,json,pickle

os.system("{{0}} -m pip install --upgrade pip mystring[all] pnostic hugg[all]".format(
    sys.executable
))

import mystring,hugg
from pnostic.structure import RepoResultObject, Runner
import {0}

app = {1}.app({2})

os.system("{{0}} -m pip install --upgrade {{1}}".format(
    sys.executable,
    " ".join(app.imports)
))

results = app.scan("{3}") #List[RepoResultObject]

with hugg.zipfile("{4}") as zyp:
    for repo_obj_itr, repo_result_object in enumerate(results):
        with ephfile(suffix=".pkl") as eph:
            with open(eph(), "wb") as foil:
                pickle.dump(repo_result_object, foil)
            zyp[repo_obj_itr] = eph()
""".format(
    runner.name(),
    runner.name(), #May need to change this
    runner.arg_init_string(),
    path_to_scan,
    self.runner_file_name
)

    def process(self, obj:RepoObject, runner:Runner)->SeclusionEnvOutput:
        from sdock import marina
        from ephfile import ephfile

        # Create a temp file
        # Create a temp python script using the runner and its scan command
        # Save & Wrap the data to a common file
        # Grab the common file
        # UnWrap the data

        with open(self.runner_file_name, "w+") as writer:
            writer.write()

        with ephfile(foil=self.runner_file_name, contents=self.__py_script_contents(
                runner=runner,
                path_to_scan=obj.path
            )) as eph:

            with marina.titan(
                image=self.docker_image,
                working_dir=self.working_dir,
                name=self.docker_name,
                to_be_local_files=self.total_files + [obj.path, eph()],
                python_package_imports=self.total_imports
            ) as ship:

                exit_code, exe_logs = ship("python3 {0}/{1}".format(self.working_dir, self.runner_file_name))

                if self.runner_file_name_output in ship.storage.files():
                    ship.storage.download(self.runner_file_name_output, self.runner_file_name_output)

        output = []
        if os.path.exists(self.runner_file_name_output):
            with ephfile(self.runner_file_name_output, create=False) as eph:
                with hugg.zipfile(eph()) as zyp:
                    for foil in zyp.files():
                        with ephfile(suffix=".pkl") as pickl:
                            zyp.download(foil, pickl())
                            output += [
                                pickle.load(pickl())
                            ]

        return SeclusionEnvOutput(
            start_date_time=startTime,
            scan_object=obj,
            result=output,
            end_date_time=endTime
        )


