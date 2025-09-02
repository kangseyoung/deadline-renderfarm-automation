import tempfile, subprocess

def submit(job_info: str, plugin_info: str, deadlinecommand: str = "deadlinecommand"):
    jf = tempfile.NamedTemporaryFile(delete=False, suffix="_job_info.txt", mode="w", encoding="utf-8")
    pf = tempfile.NamedTemporaryFile(delete=False, suffix="_plugin_info.txt", mode="w", encoding="utf-8")
    jf.write(job_info); jf.close()
    pf.write(plugin_info); pf.close()

    cmd = [deadlinecommand, "SubmitJob", jf.name, pf.name]
    res = subprocess.run(cmd, capture_output=True, text=True)
    return (res.returncode == 0), res.stdout, res.stderr
