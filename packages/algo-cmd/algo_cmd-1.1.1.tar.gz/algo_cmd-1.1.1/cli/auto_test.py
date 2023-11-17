import argparse
import json
import os
import sys

from cmd_request.CMD_REQUEST import REQUEST


class PROJECT_CFG:
    RS_TOKEN = os.environ.get('RS_TOKEN', 'demo')
    NUZ_TOKEN = os.environ.get('NUZ_TOKEN', 'demo')
    GIT_HOST = os.environ.get('GIT_HOST', 'demo')
    PRO_URL = GIT_HOST + "/api/v4/projects/{}/trigger/pipeline"


def main():
    if PROJECT_CFG.RS_TOKEN == 'demo' or PROJECT_CFG.NUZ_TOKEN == 'demo' or PROJECT_CFG.GIT_HOST == 'demo':
        print("请设置环境变量，需要设置 rs token/nuz token/ git仓库域名")
        print("========================================")
        print("参考：export RS_TOKEN=xxxx")
        print("参考：export NUZ_TOKEN=xxxx")
        print("参考：export GIT_HOST=xxxx")
        print("========================================")

        sys.exit(-1)
    parser = argparse.ArgumentParser(description='触发接口自动化')
    parser.add_argument(
        "-p", "--project", dest="project", help="entry project name，demo is : -p rs or -p nuz"
    )
    parser.add_argument(
        "-b", "--branch", dest="branch", help="entry branch demo is  master"
    )
    args = parser.parse_args()
    project, branch = 'rs', 'master'
    if args.project:
        project = args.project
    if args.branch:
        branch = args.branch

    if project == 'rs':
        api_token = PROJECT_CFG.RS_TOKEN
        project_id = 61003
    if project == 'nuz':
        api_token = PROJECT_CFG.NUZ_TOKEN
        project_id = 76206

    payload = {'token': api_token,
               'ref': str(branch),
               'variables[CI_COMMIT_MESSAGE]': 'auto_api'}
    response = None
    page_url = None
    try:
        response = REQUEST().gen_client().post(PROJECT_CFG.PRO_URL.format(str(project_id)), data=payload).json()
        if project == 'rs':
            page_url = PROJECT_CFG.GIT_HOST + "/shopee/marketing/opa-algo/rcmdsys/engine-server/-/pipelines/{}".format(
                response['id'])
        if project == 'nuz':
            page_url = PROJECT_CFG.GIT_HOST + "/shopee/marketing/opa-algo/rcmdsys/nuz/nuzrcmd/-/pipelines/{}".format(
                response['id'])
    except Exception:
        msg = {
            "exec_info：": "error",
            "exec_code：": -1
        }

    if response and response['status'] == 'created' and page_url:
        msg = {
            "cicd_page": page_url,
            "report": " check it on seatalk noti"
        }
    print(json.dumps(msg, indent=4))

    sys.exit(0)


if __name__ == '__main__':
    main()
