from setuptools import setup, find_packages

setup(name='personal_assistant',
      version='0.0.1',
      description='Your personal assistant',
      url='https://github.com/Kateryna-Shylina/pc_project_group_04',
      author='GoIt Python21 project_group_04',
      packages=find_packages(),
      entry_points={
          'console_scripts':['personal-assistant=src.user_interface:start_bot']
      }
    )