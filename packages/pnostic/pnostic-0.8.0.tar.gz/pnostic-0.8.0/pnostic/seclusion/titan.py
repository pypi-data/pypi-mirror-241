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

    def clean(self) -> bool:
        return True

    def python_packages(self,packages:List[str]) -> bool:
        self.total_imports.extend(packages)
        return True

    def setup_files(self,files:List[str]) -> bool:
        self.total_files.extend(files)
        return True

    def process(self, obj:RepoObject, runner:Runner)->SeclusionEnvOutput:
        from sdock import marina

        with marina.titan(image=self.docker_image,working_dir=self.working_dir,name=self.docker_name) as ship:
            with ship.storage() as store:
                store.upload(local_cryptolation, "cryptolation.zip")
                store.upload(file_path, os.path.basename(file_path))

                exit_code, exe_logs = ship(cmd_string)
                if exit_code != 0:
                    logger.info("potential issue with the run")
                with open("rawlogs_{0}.txt".format(eph()), "w+") as writer:
                    print("".join(exe_logs))
                    for log in exe_logs:
                        logger.info(log)
                        writer.write(log + "\n")

                logger.info("current files: [{0}]".format(', '.join(store.files())))
                try:
                    if base_result_file in store.files():
                        store.download(result_file, base_result_file)
                        exists = True
                except Exception as e:
                    print(">|>")
                    print(e)

        import ephfile,mystring
        startTime,endTime,output="","",[]

        with ephfile.ephfile(contents = obj.content) as eph:
            path_to_scan = None
            if obj.content is None:
                path_to_scan = obj.path
            else:
                path_to_scan = eph()

            try:
                startTime = mystring.current_date()
                output = runner.scan(path_to_scan)
                endTime = mystring.current_date()
            except Exception as e:
                _, _, exc_tb = sys.exc_info();fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                output = [RepoResultObject.newEmpty(
                    projecttype=obj.path,
                    projectname=obj.path,
                    projecturl=None,
                    qual_name=None,
                    tool_name=runner.name(),
                    stage=None,
                    ExceptionMsg=":> Hit an unexpected error {0} @ {1}:{2}".format(e, fname, exc_tb.tb_lineno),
                    startDateTime=None,
                    endDateTime=None
                )]

        return SeclusionEnvOutput(
            start_date_time=startTime,
            scan_object=obj,
            result=output,
            end_date_time=endTime
        )