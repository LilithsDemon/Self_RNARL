#!/usr/bin/env python
# coding: utf-8

# In[1]:


from learnamaster.src import learna
from learnamaster.src.learna import agent, design_rna, environment_test, environment, learn_to_design_rna
from learnamaster.src.data import download_and_build_eterna
from learnamaster.utils import timed_execution
from pandas import read_csv
import numpy as np


# In[2]:


# Fetch Eterna Dataset
# download_and_build_eterna.download_eterna("learnastuffhere/eterna.txt")
download_and_build_eterna.extract_secondarys("learnastuffhere/eterna.txt", "learnastuffhere/eternadumper.txt")
data = read_csv("learnastuffhere/eterna.txt", delimiter='\t')


# In[3]:


structure_data = data[["Secondary Structure"]].values
structure_data = structure_data
structures = []
for struct in structure_data:
    struct = str(struct)
    cleaned_string = struct.replace("[", "").replace("]", "").replace("'", "").replace("_", "")
    structures.append(cleaned_string)


# In[4]:


# Get Environment, No conv, No embedding
env_conf = environment.RnaDesignEnvironmentConfig(use_conv=False, use_embedding=False, state_radius=10)
real_env_conf = environment.RnaDesignEnvironment(structures,env_conf)


# In[5]:


# Get Agent Configuration
agent_conf = agent.AgentConfig()
# Get Network Configuration
network_conf = agent.NetworkConfig()


# In[6]:


# Create regular LEARNA model
learn_to_design_rna.learn_to_design_rna(structures, timeout=100, worker_count=1,
                                        save_path="learnamaster/models/ICLR_2019/224_0_1/",
                                        restore_path=None, #"learnamaster/models/ICLR_2019/224_0_1/",
                                        network_config=network_conf,
                                        agent_config=agent_conf,
                                        env_config=env_conf)


# In[ ]:




