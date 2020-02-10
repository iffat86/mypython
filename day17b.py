import configparser


config  = configparser.ConfigParser()

config["DEFAULT"] = {'Server alive interval':"45","Compression":"yes","CompressionLevel": "9"}
config["bitbucket.org"] = {}
config["bitbucket.org"]["User"] = "hg"
config["topsecret.server.com"] = {}
topsecret = config["topsecret.server.com"]
topsecret["Port"] = "50022"
topsecret["ForwardX11"] = "no"
config['DEFAULT']["ForwardX11"] = "yes"
with open ('config.cfg',"w") as configfile:
    config.write(configfile)