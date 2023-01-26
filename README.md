# vt-parser-ssh
# Introduction 
[![LICENSE](https://badgen.net/badge/license/MIT/blue)](LICENSE.md)

This is a small but useful script that allow user to use the nix* ssh logs for IP based threat intelligence queries to virus total. The output of the script is in json format.

# Use

The code is compiled using [Pycharm](https://www.jetbrains.com/pycharm/)

You can trying running the script using python terminal or the terminal

`python3 .\vr-parser-ssh.py`

#NOTE Make sure you have ssh logs with you, for sample you can try downloading sample [SSH](https://raw.githubusercontent.com/elastic/examples/master/Machine%20Learning/Security%20Analytics%20Recipes/suspicious_login_activity/data/auth.log)

Make sure you have replaced the API key in code over here

`headers = {
    "accept": "application/json",
    "x-apikey": "#REPLACEME#"
}`

# Output

```{
  "indicators": [
    {
      "value": "119.63.130.84",
      "type": "ip"
    }
  ]
} {
  "providers": [
    {
      "provider": "['Bkav']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['CMC Threat Intelligence']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['Snort IP sample list']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['0xSI_f33d']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['ViriBack']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['PhishLabs']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['K7AntiVirus']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['CINS Army']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['Quttera']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['PrecisionSec']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['OpenPhish']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['VX Vault']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['Web Security Guard']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['Scantitan']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['AlienVault']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['Sophos']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['Phishtank']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['Cyan']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['Spam404']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['SecureBrain']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['Hoplite Industries']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['CRDF']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['Fortinet']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['alphaMountain.ai']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['Lionic']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['Cyble']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['Seclookup']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['Xcitium Verdict Cloud']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['Virusdie External Site Scan']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['Google Safebrowsing']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['SafeToOpen']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['ADMINUSLabs']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['CyberCrime']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['Juniper Networks']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['Heimdal Security']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['AutoShun']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['Trustwave']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['AICC (MONITORAPP)']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['CyRadar']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['Dr.Web']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['Emsisoft']",
      "verdict": "['harmless']",
      "score": "['clean']"
    },
    {
      "provider": "['Abusix']",
      "verdict": "['harmless']",
      "score": "['clean']"
    }
  ]
}


