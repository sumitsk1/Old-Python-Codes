from cx_Freeze import setup , Executable
setup (name = "pytoexe",
       version= "0.1" ,
       description = "you can convert py to exe" ,
       executables = [Executable (r"C:\my file\python\calculator.py")]
       )
