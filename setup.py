from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='vifaniyalviv.policy',
      version=version,
      description="vifaniyalviv project",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['vifaniyalviv'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.usernamelogger',
          'iw.rotatezlogs',
          'collective.xsendfile',
          'plone.app.caching',
          'plone.app.theming',
          'Products.Carousel',
          'Products.PloneFormGen',
          'Products.PloneGlossary',
          'collective.embedly',
          'quintagroup.dropdownmenu',
          'quintagroup.plonecaptchas',
          'quintagroup.seoptimizer',
          'quintagroup.portlet.cumulus',
#          'beyondskins.responsive',
          'collective.quickupload',
          'Products.Ploneboard',
          'cioppino.twothumbs',
          'Products.ContentWellPortlets',
          'collective.panels',
#          'collective.easyslider',
#          'collective.prettyphoto',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
