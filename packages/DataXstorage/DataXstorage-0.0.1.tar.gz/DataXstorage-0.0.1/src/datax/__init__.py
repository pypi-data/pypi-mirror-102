import os


dirname =   "DATAX_API_FILES"

def store_new_content(filename,jsontrue,name,f1 = None,f2 = None,f3 = None,*arg):


  if os.path.exists(f"{dirname}"):
    file1 = open(f"{dirname}/{filename}.txt","w")
    fulllist = [name,f1,f2,f3, *arg]
    varlist = ':'.join(fulllist)
    file1.write(f"{varlist} \n")
    file1.close()
    return
  else:
    os.system(f"mkdir {dirname}")

    file1 = open(f"{dirname}/{filename}.txt","w")
    fulllist = [name,f1,f2,f3, *arg]
    varlist = ':'.join(fulllist)
    file1.write(f"{varlist} \n")
    file1.close()
    return


def add_content(filename,name,f1 = None,f2 = None,f3 = None,*arg):
  if os.path.exists(f"{dirname}"):


    file1 = open(f"{dirname}/{filename}.txt","a")

    fulllist = [name,f1,f2,f3, *arg]
    varlist = ':'.join(fulllist)

    file1.write(f"{varlist}")

    file1.close()
    return
  else:
    os.system(f"mkdir {dirname}")

    file1 = open(f"{dirname}/{filename}.txt","a")

    fulllist = [name,f1,f2,f3, *arg]
    varlist = ':'.join(fulllist)

    file1.write(f"{varlist}")

    file1.close()

    file2 = open(f"{dirname}/{filename}.txt","a")

    file2.write(f"\n")

    return



def show_content(filename):
  if os.path.exists(f"{dirname}"):

    file1 = open(f"{dirname}/{filename}.txt","r")
    print(file1.read())

    file1.close()
    return
  else:
    os.system(f"mkdir {dirname}")
    file1 = open(f"{dirname}/{filename}.txt","r")
    print(file1.read())

    file1.close()
    return




def kill_file(filename):

  if os.path.exists(f"{dirname}"):

    if os.path.exists(f"{dirname}/{filename}.txt"):
      os.remove(f"{dirname}/{filename}.txt")

      return
    else:
      print(f"[DATAX API]The file named {filename}.txt does NOT exist,cant delete")
      return
  else:
    os.system(f"mkdir {dirname}")

    if os.path.exists(f"{dirname}/{filename}.txt"):
      os.remove(f"{dirname}/{filename}.txt")
      return
    else:
      print(f"[DATAX API]The file named {filename}.txt does NOT exist,cant delete")
      return


def kill_content(filename):
  if os.path.exists(f"{dirname}"):

    file1 = open(f"{dirname}/{filename}.txt","w")
    file1.close()
  else:
    os.system(f"mkdir {dirname}")
    file1 = open(f"{dirname}/{filename}.txt","w")
    file1.close()


#json edition

def json_store_new_content(filename,name,f1 = None,f2 = None,f3 = None,*arg):
  if os.path.exists(f"{dirname}"):

    file1 = open(f"{dirname}/{filename}.json","w")
    file1.write("{ \n")

    fulllist = [name,f1,f2,f3, *arg]
    varlist = ':'.join(fulllist)

    file1.write(f'"{varlist}" : "dataxapi" \n')
    file1.write("},\n")

    file1.close()
    return
  else:
    os.system(f"mkdir {dirname}")
    file1 = open(f"{dirname}/{filename}.json","w")
    file1.write("{ \n")

    fulllist = [name,f1,f2,f3, *arg]
    varlist = ':'.join(fulllist)

    file1.write(f'"{varlist}" : "dataxapi" \n')
    file1.write("},\n")

    file1.close()
    return



def json_add_content(filename,name,f1 = None,f2 = None,f3 = None,*arg):
  if os.path.exists(f"{dirname}"):
  

    file1 = open(f"{dirname}/{filename}.json","a")
    file1.write("{ \n")

    fulllist = [name,f1,f2,f3, *arg]
    varlist = ':'.join(fulllist)

    file1.write(f'"{varlist}" : "dataxapi" \n')
    file1.write("},\n")

    file1.close()
    return

  else:
    os.system(f"mkdir {dirname}")
    file1 = open(f"{dirname}/{filename}.json","a")
    file1.write("{ \n")

    fulllist = [name,f1,f2,f3, *arg]
    varlist = ':'.join(fulllist)

    file1.write(f'"{varlist}" : "dataxapi" \n')
    file1.write("},\n")

    file1.close()
    return

def json_show_content(filename):
  if os.path.exists(f"{dirname}"):
    file1 = open(f"{dirname}/{filename}.json","r")
    print(f"JSON IS STILL IN BETA,IT MAY HAVE ERORS \n{file1.read()}")
    file1.close()
    return
  else:
    os.system(f"mkdir {dirname}")
    file1 = open(f"{dirname}/{filename}.json","r")
    print(f"JSON IS STILL IN BETA,IT MAY HAVE ERORS \n{file1.read()}")

    file1.close()
    return

def json_kill_file(filename):
  if os.path.exists(f"{dirname}"):

    if os.path.exists(f"{filename}.json"):
      os.remove(f"{filename}.json")
      return
    else:
      print(f"[DATAX API]The file named {filename}.json does NOT exist,cant delete")
      return
  else:
    os.system(f"mkdir {dirname}")

    if os.path.exists(f"{filename}.json"):
      os.remove(f"{filename}.json")
      return
    else:
      print(f"[DATAX API]The file named {filename}.json does NOT exist,cant delete")
      return


def json_kill_content(filename):
  file1 = open(f"{filename}.json","w")
  file1.close()
