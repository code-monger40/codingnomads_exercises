# Use the built-in `platform` module to print out the following info:
import platform

placeholder = platform
 
print(f"{'Platform:':>10} {placeholder.platform()}",)  # platform.platform()
print(f"{'Compiler:':>10} {placeholder.python_compiler()}",)  # platform.python_compiler()
print(f"{'Python:':>10} {placeholder.python_version()}",)  # platform.python_version()
print(f"{'System:':>10} {placeholder.system()}",)  # platform.system()
print(f"{'Release:':>10} {placeholder.release()}",)  # platform.release()
print(f"{'System:':>10} {placeholder.processor()}",)  # platform.processor()