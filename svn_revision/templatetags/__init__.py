def get_revision():
    from subprocess import check_output, PIPE
    import re
    import os
    import logging
    log = logging.getLogger("svn_revision")

    result = "Versioning Unavailable"
    try:
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../../")
        outS = check_output([ 'svnversion', path ])
        m = re.match('(\d+:?\d*[MS]?)$', outS)
        if m and m.group(1):
            result = 'r' + m.group(1)
        else:
            log.warn("Didn't like SVN output %s", outS)
    except:
        log.exception("Failed to call SVN")

    return result

REVISION = get_revision()
