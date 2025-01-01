import glob, os, shutil, fileinput
import datetime


sep = os.sep

Import("env", "projenv")
print("Post build scripts > sdl2_build_extra.py")

def after_upload(source, target, env):
    
    env_prog = str(source[0]).split(sep)[-1]
    env_name = str(source[0]).split(sep)[-2]
    print(f"Copying file from action {target[0]} for {env_name}")

    dest_dir = f"test{sep}{env_name}"
    os.makedirs(dest_dir, exist_ok=True)

    shutil.copyfile(f".pio{sep}build{sep}{env_name}{sep}{env_prog}", f"test{sep}{env_name}{sep}{env_prog}")
    e = datetime.datetime.now()
    print (e.strftime("%H:%M:%S %d-%m-%Y"))
    
    
    
env.AddPostAction("upload", after_upload)
env.AddPostAction("buildprog", after_upload)