import setuptools

setuptools.setup(
    name='equoai_node',
    version='1.0.0',
    author='David Hostler',
    description='Quickly improve and scale the quality of your LLM applications with the EquoAI Clientside API!',
    packages=['equoai_node'],
    download_url = 'https://github.com/DavidHostler/equoai_node-v2',    # I explain this later on
    install_requires=[            # I get to this in a second
          'requests',
          'tiktoken'
      ],
)
