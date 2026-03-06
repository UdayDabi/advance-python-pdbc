import shutil

source = "C:/Users/udayd/OneDrive/Desktop/IO/Rays.png";
target = "C:/Users/udayd/OneDrive/Desktop/Op/Rays3.png";

shutil.copyfile(source, target)
print(source + " is copied to " + target)
