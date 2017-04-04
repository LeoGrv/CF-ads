# -*- coding: utf-8 -*-
#!/usr/bin/python
import logging
import time
from googleads import adwords
import json
import requests
import re
import get_campaigns
import get_ad_groups
import json_parse
import ad_group_stop
#auth info
adwords_client = adwords.AdWordsClient.LoadFromStorage('/Users/leo/Documents/Obuchenie/AdWordsPython/googleads.yaml')

#get feed
rest_feed = json_parse.main()
#get all campaigns
campaigns_feed = get_campaigns.main(adwords_client)
#get list of dicts of ad groups in campaigns, dict(Ad group NAME:Ad group ID)
ads_group_feed = {}
for campaign in campaigns_feed:
	ads_group_feed.update(get_ad_groups.main(adwords_client,campaign))

for ad_group_name in ads_group_feed:
	for rest in rest_feed:
		rest_id = '[%s]' % rest['id'] 
		if rest_id in ad_group_name:
			if rest['status'] == 'active':
				ad_group_stop.main(adwords_client,str(ads_group_feed[ad_group_name]),'ENABLED')
			elif rest['status'] != 'active':
				ad_group_stop.main(adwords_client,str(ads_group_feed[ad_group_name]),'PAUSED')