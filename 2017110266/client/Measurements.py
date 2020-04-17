import delegator
import lauda
import logging
import statistics


class Measurement:

    def __init__(self, _language, _version_cmd, _run_cmd, _compile_cmd = None, _debug = False):
        self.language = _language
        self.version_cmd = _version_cmd
        self.run_cmd = _run_cmd
        self.compile_cmd = _compile_cmd
        self.debug = _debug
        self.results = {"name" : self.language}

    def run(self):

        print(f"[{self.language}]")

        if self.compile_cmd:
            cmd_compile = delegator.run(self.compile_cmd)  
            if self.debug or cmd_compile.return_code is not 0:
                logging.info(cmd_compile.out)

        print(f"Version :  {delegator.run(self.version_cmd).out.splitlines()[0]}")

        times = []
        count = 0

        while count < 10:
            count += 1

            stopWatch = lauda.StopWatch()
            stopWatch.start()
            delegator.run(self.run_cmd)
            stopWatch.stop()
            times.append(int(stopWatch.elapsed_time * 1000))
        
        print(f"Speed (all): {'ms, '.join(map(str, times))}ms")
        print(f"Speed (best): {min(times)}ms")
        print(f"Speed (worst): {max(times)}ms")
        print(f"Speed (median): {statistics.median(times)}ms")

        print('\n')