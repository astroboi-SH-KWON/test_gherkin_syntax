# test_gherkin_syntax
https://behave.readthedocs.io/en/latest/

# Setting up the Environment  
    1. Set conda env
        if silicon mac:
            conda create -n behave python==3.8.5
            conda activate behave
            
            pip install behave==1.2.6

            # # Installing pyhamcrest from the conda-forge channel can be achieved by adding conda-forge to your channels with:
            conda config --add channels conda-forge
            conda config --set channel_priority strict
            # # It is possible to list all of the versions of pyhamcrest available on your platform with conda:
            conda search pyhamcrest --channel conda-forge
            conda install pyhamcrest==2.0.4


# Tutorial
* https://behave.readthedocs.io/en/latest/tutorial/

# Features
* behave operates on directories containing:
1. feature files written by your Business Analyst / Sponsor / whoever with your behaviour scenarios in it, and
   * feature files : https://behave.readthedocs.io/en/latest/tutorial/#feature-files
2. a “steps” directory with Python step implementations for the scenarios.
   * Python step implementations : https://behave.readthedocs.io/en/latest/tutorial/#python-step-implementations
3. 
