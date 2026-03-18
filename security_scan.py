import os

def check_hardcoded_password(file):
    issues=[]
    with open(file,"r",errors="ignore") as f:
        for i,line in enumerate(f.readlines()):
            if "password" in line.lower():
                issues.append(f"{file}: Line {i+1} -> Possible hardcoded password")
    return issues

def scan_project():
    results=[]

    for root,dirs,files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                filepath=os.path.join(root,file)
                results.extend(check_hardcoded_password(filepath))
    return results

if __name__=="__main__":
    findings=scan_project()

    if findings:
        print(" Security Issues Found:\n")
        for issue in findings:
            print(issue)
        exit(1)
    else:
        print("No Major issues found")