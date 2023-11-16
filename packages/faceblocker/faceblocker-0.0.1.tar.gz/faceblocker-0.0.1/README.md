
# Table of Contents

1.  [Building instructions](#org9b55c85)
    1.  [structurey](#org797390d)
    2.  [pyproject and MANIFEST](#orgf41cc25)


<a id="org9b55c85"></a>

# Building instructions


<a id="org797390d"></a>

## structurey

    pwd
    tree -I "envs|dist" --matchdirs ./


<a id="orgf41cc25"></a>

## pyproject and MANIFEST

    [project]
    name = "faceblocker"
    version = "0.0.1"
    authors = [
    {name="Rita Collins", email="r.collins3730@gmail.com" },
    ]
    description = "A CLI tool that can remove faces from videos and replace them with images."
    readme = "README.md"
    requires-python = ">=3.11"
    dependencies = [
    "moviepy<2.0",
    "opencv>4.0.0",
    ]
    classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ]
    
    [project.urls]
    "Homepage" = "https://gitlab.com/rdotcollins/movie-anonymiser"
    "Bug Tracker" = "https://gitlab.com/rdotcollins/movie-anonymiser/issues"
    
    #[tool.setuptools.packages]
    #find = {}  # Scan the project directory with the default parameters
    [tool.setuptools]
    include-package-data = true
    # OR
    [tool.setuptools.dynamic]
    readme = {file = ["README.org"]}
    [tool.setuptools.packages.find]
    # All the following settings are optional:
    where = ["src"]  # ["."] by default
    include = ["*"]  # ["*"] by default
    
    [project.scripts] 
    faceblocker = "faceblocker.faceblocker:main"
    
    [build-system]
    requires = ["setuptools >= 61.0"]
    build-backend = "setuptools.build_meta"

    # Command Description
    # include pat1 pat2 ... Add all files matching any of the listed patterns (Files must be given as paths relative to the root of the project)
    # exclude pat1 pat2 ... Remove all files matching any of the listed patterns (Files must be given as paths relative to the root of the project)
    # recursive-include dir-pattern pat1 pat2 ... Add all files under directories matching dir-pattern that match any of the listed patterns
    recursive-include ./yunet_model/
    # recursive-exclude dir-pattern pat1 pat2 ... Remove all files under directories matching dir-pattern that match any of the listed patterns
    # global-include pat1 pat2 ... Add all files anywhere in the source tree matching any of the listed patterns
    # global-exclude pat1 pat2 ... Remove all files anywhere in the source tree matching any of the listed patterns
    # graft dir-pattern Add all files under directories matching dir-pattern
    # prune dir-pattern Remove all files under directories matching dir-pattern
    # The patterns here are glob-style patterns: * matches zero or more regular filename characters (on Unix, everything except forward slash; on Windows, everything except backslash and colon); ? matches a single regular filename character, and [chars] matches any one of the characters between the square brackets (which may contain character ranges, e.g., [a-z] or [a-fA-F0-9]). Setuptools also has undocumented support for ** matching zero or more characters including forward slash, backslash, and colon.
    # Directory patterns are relative to the root of the project directory; e.g., graft example* will include a directory named examples in the project root but will not include docs/examples/.

