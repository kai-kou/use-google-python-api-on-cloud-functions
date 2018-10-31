from googleapiclient import discovery

from httplib2 import Http

from oauth2client.client import GoogleCredentials


def check_discovery_error(request):
  # Cloud Functions環境から認証情報を取得する
  credentials = GoogleCredentials.get_application_default()

  cloudBuild = discovery.build(
    'cloudbuild', 'v1',    # Cloud Buildじゃなく、他のサービスでもおｋ
    http=credentials.authorize(Http()),
    cache_discovery=False) # cache_discovery=Falseしてエラーを回避する

  request = cloudBuild.projects().builds().list(projectId='[GCPのプロジェクトID]')
  response = request.execute()
  print(response)