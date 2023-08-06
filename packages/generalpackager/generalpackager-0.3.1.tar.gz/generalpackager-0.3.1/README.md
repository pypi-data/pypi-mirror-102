# generalpackager
Tools to interface GitHub, PyPI and local modules / repos. Used for generating files to keep projects dry and synced. Tailored for my general packages.

This package and 3 other make up [ManderaGeneral](https://github.com/Mandera).

## Information
| Package                                                              | Ver                                                | Latest Release        | Python                                                                                                                   | Platform        |   Lvl | Todo                                                        | Tests   |
|:---------------------------------------------------------------------|:---------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------------|:----------------|------:|:------------------------------------------------------------|:--------|
| [generalpackager](https://github.com/ManderaGeneral/generalpackager) | [0.3.1](https://pypi.org/project/generalpackager/) | 2021-04-14 18:44 CEST | [3.8](https://www.python.org/downloads/release/python-380/), [3.9](https://www.python.org/downloads/release/python-390/) | Windows, Ubuntu |     2 | [6](https://github.com/ManderaGeneral/generalpackager#Todo) | 100.0 % |

## Contents
<pre>
<a href='#generalpackager'>generalpackager</a>
├─ <a href='#Information'>Information</a>
├─ <a href='#Contents'>Contents</a>
├─ <a href='#Installation'>Installation</a>
├─ <a href='#Attributes'>Attributes</a>
└─ <a href='#Todo'>Todo</a>
</pre>

## Installation
| Command                       | <a href='https://pypi.org/project/pandas'>pandas</a>   | <a href='https://pypi.org/project/generallibrary'>generallibrary</a>   | <a href='https://pypi.org/project/generalfile'>generalfile</a>   | <a href='https://pypi.org/project/gitpython'>gitpython</a>   | <a href='https://pypi.org/project/requests'>requests</a>   |
|:------------------------------|:-------------------------------------------------------|:-----------------------------------------------------------------------|:-----------------------------------------------------------------|:-------------------------------------------------------------|:-----------------------------------------------------------|
| `pip install generalpackager` | Yes                                                    | Yes                                                                    | Yes                                                              | Yes                                                          | Yes                                                        |

## Attributes
<pre>
<a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/__init__.py#L1'>Module: generalpackager</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L13'>Class: GitHub</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L31'>Method: download</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L27'>Method: exists</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L80'>Method: get_description</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L50'>Method: get_owners_packages</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L68'>Method: get_topics</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L58'>Method: get_website</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/shared.py#L4'>Method: is_general</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L86'>Method: set_description</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L74'>Method: set_topics</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L64'>Method: set_website</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L9'>Class: LocalModule</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L23'>Method: exists</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L64'>Method: get_all_local_modules</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L75'>Method: get_dependants</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L70'>Method: get_dependencies</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L55'>Method: get_env_vars</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/shared.py#L4'>Method: is_general</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L33'>Property: module</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L42'>Property: objInfo</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L22'>Class: LocalRepo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L165'>Method: bump_version</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L178'>Method: create_sdist</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L194'>Property: description</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L194'>Property: enabled</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L63'>Method: exists</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L194'>Property: extras_require</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L131'>Method: get_git_exclude_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L134'>Method: get_license_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L133'>Method: get_manifest_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L130'>Method: get_metadata_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L152'>Method: get_package_paths_gen</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L96'>Method: get_path_from_name</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L129'>Method: get_readme_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L83'>Method: get_repo_path_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L75'>Method: get_repo_path_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L88'>Method: get_repos_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L132'>Method: get_setup_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L136'>Method: get_test_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L140'>Method: get_test_paths</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L135'>Method: get_workflow_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L160'>Method: git_changed_files</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L44'>Method: has_metadata</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L194'>Property: install_requires</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/shared.py#L4'>Method: is_general</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L47'>Method: load_metadata</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L194'>Property: manifest</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L194'>Property: name</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L68'>Method: path_exists</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L169'>Method: pip_install</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L145'>Method: text_in_tests</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L194'>Property: topics</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L174'>Method: unittest</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L183'>Method: upload</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L194'>Property: version</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L23'>Class: Packager</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_github.py#L20'>Method: commit_and_push</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L83'>Method: compare_local_to_github</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L90'>Method: compare_local_to_pypi</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L50'>Method: exists</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L62'>Method: filter_relative_filenames</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L19'>Method: general_bumped_set</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L25'>Method: general_changed_dict</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L154'>Method: generate_git_exclude</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L160'>Method: generate_license</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L242'>Method: generate_localfiles</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L145'>Method: generate_manifest</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L218'>Method: generate_personal_readme</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L188'>Method: generate_readme</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L97'>Method: generate_setup</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L172'>Method: generate_workflow</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L188'>Method: get_attributes_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L10'>Method: get_badges_dict</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_metadata.py#L26'>Method: get_classifiers</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L79'>Method: get_description_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L69'>Method: get_env</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L194'>Method: get_footnote_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L85'>Method: get_information_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L114'>Method: get_installation_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_pypi.py#L6'>Method: get_latest_release</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L6'>Method: get_ordered_packagers</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L13'>Method: get_owners_package_names</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L103'>Method: get_sync_job</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L63'>Method: get_todos</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L70'>Method: get_todos_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_metadata.py#L16'>Method: get_topics</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L22'>Method: get_triggers</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L89'>Method: get_unittest_job</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L33'>Method: get_untested_objInfo_dict</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L148'>Method: github_link</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L157'>Method: github_link_path_line</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L156'>Method: if_publish_bump</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L163'>Method: if_publish_publish</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_metadata.py#L32'>Method: is_bumped</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/shared.py#L4'>Method: is_general</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L46'>Method: relative_path_is_aesthetic</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L119'>Method: run_ordered_methods</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L54'>Method: spawn_children</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L57'>Method: spawn_parents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L44'>Method: step_install_necessities</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L59'>Method: step_install_package_git</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L51'>Method: step_install_package_pip</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L112'>Method: step_run_packager_method</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L37'>Method: step_setup_python</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L80'>Method: steps_setup</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_github.py#L12'>Method: sync_github_metadata</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L134'>Method: workflow_sync</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L126'>Method: workflow_unittest</a>
└─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L25'>Class: PyPI</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L49'>Method: download</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L39'>Method: exists</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L70'>Method: get_date</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L61'>Method: get_owners_packages</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L43'>Method: get_tarball_url</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L65'>Method: get_version</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/shared.py#L4'>Method: is_general</a>
   └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L75'>Method: reserve_name</a>
</pre>

## Todo
| Module                                                                                                                             | Message                                                                                                                                                                                                  |
|:-----------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L1'>local_repo.py</a>     | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L24'>Search for imports to list dependencies.</a>                                               |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L1'>pypi.py</a>                 | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L11'>Move download to it's own package.</a>                                                           |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L1'>pypi.py</a>                 | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L67'>Find a faster fetch for latest PyPI version.</a>                                                 |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L1'>pypi.py</a>                 | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L72'>Find a faster fetch for latest PyPI datetime.</a>                                                |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L1'>packager.py</a>             | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L4'>Add a check in workflow to make sure it doesn't use a pypi version in case of wrong order.</a>    |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L1'>packager_files.py</a> | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L30'>Watermark generated files to prevent mistake of thinking you can modify them directly.</a> |

<sup>
Generated 2021-04-14 18:44 CEST for commit <a href='https://github.com/ManderaGeneral/generalpackager/commit/5d3ae3b'>5d3ae3b</a>.
</sup>
