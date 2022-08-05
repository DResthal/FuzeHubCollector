import scrapy
import json
from pprint import pprint


class PrintablesSpider(scrapy.Spider):
    name = "printables"
    allowed_domains = ["printables.com"]
    start_urls = ["https://www.printables.com/graphql/"]

    def start_requests(self):
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en",
            "content-type": "application/json",
            "operation": "PrintList",
            "referer": "https://www.printables.com/model",
        }

        data = {
            "operationName": "PrintList",
            "variables": {
                "limit": 36,
                "categoryId": None,
                "publishedDateLimitDays": None,
                "hasMake": False,
                "competitionAwarded": False,
                "featured": False,
                "likedByMe": False,
                "collectedByMe": False,
                "madeByMe": False,
                "ordering": "-download_count_7_days",
                "cursor": None,
            },
            "query": "query PrintList($limit: Int!, $cursor: String, $categoryId: ID, $materialIds: [Int], $userId: ID, $printerIds: [Int], $licenses: [ID], $ordering: String, $hasModel: Boolean, $filesType: [FilterPrintFilesTypeEnum], $includeUserGcodes: Boolean, $nozzleDiameters: [Float], $weight: IntervalObject, $printDuration: IntervalObject, $publishedDateLimitDays: Int, $featured: Boolean, $featuredNow: Boolean, $usedMaterial: IntervalObject, $hasMake: Boolean, $competitionAwarded: Boolean, $onlyFollowing: Boolean, $collectedByMe: Boolean, $madeByMe: Boolean, $likedByMe: Boolean) {\n  morePrints(\n    limit: $limit\n    cursor: $cursor\n    categoryId: $categoryId\n    materialIds: $materialIds\n    printerIds: $printerIds\n    licenses: $licenses\n    userId: $userId\n    ordering: $ordering\n    hasModel: $hasModel\n    filesType: $filesType\n    nozzleDiameters: $nozzleDiameters\n    includeUserGcodes: $includeUserGcodes\n    weight: $weight\n    printDuration: $printDuration\n    publishedDateLimitDays: $publishedDateLimitDays\n    featured: $featured\n    featuredNow: $featuredNow\n    usedMaterial: $usedMaterial\n    hasMake: $hasMake\n    onlyFollowing: $onlyFollowing\n    competitionAwarded: $competitionAwarded\n    collectedByMe: $collectedByMe\n    madeByMe: $madeByMe\n    liked: $likedByMe\n  ) {\n    cursor\n    items {\n      ...PrintListFragment\n      printer {\n        id\n        __typename\n      }\n      user {\n        rating\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment PrintListFragment on PrintType {\n  id\n  name\n  slug\n  ratingAvg\n  likesCount\n  liked\n  datePublished\n  dateFeatured\n  firstPublish\n  userGcodeCount\n  downloadCount\n  category {\n    id\n    path {\n      id\n      name\n      __typename\n    }\n    __typename\n  }\n  modified\n  images {\n    ...ImageSimpleFragment\n    __typename\n  }\n  filesType\n  hasModel\n  nsfw\n  user {\n    ...AvatarUserFragment\n    __typename\n  }\n  ...LatestCompetitionResult\n  __typename\n}\n\nfragment AvatarUserFragment on UserType {\n  id\n  publicUsername\n  avatarFilePath\n  slug\n  badgesProfileLevel {\n    profileLevel\n    __typename\n  }\n  __typename\n}\n\nfragment LatestCompetitionResult on PrintType {\n  latestCompetitionResult {\n    placement\n    competitionId\n    __typename\n  }\n  __typename\n}\n\nfragment ImageSimpleFragment on PrintImageType {\n  id\n  filePath\n  rotation\n  __typename\n}\n",
        }

        for url in self.start_urls:
            yield scrapy.Request(
                url=url,
                method="POST",
                body=json.dumps(data).encode("utf-8"),
                dont_filter=True,
                headers=headers,
            )

    def parse(self, response):
        data = json.loads(response.body)
        with open('tempfile', 'w') as f:
            f.write(json.dumps(data, indent=2, sort_keys=False))
