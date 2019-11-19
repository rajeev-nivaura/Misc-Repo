from selenium import webdriver
import re
import pandas as pd
import os
import time
from tqdm import tqdm_notebook as tqdm
from .matchmaker_extract import MatchmakerExtract

def PageScrape(scrape_url,driver,save=False,save_dir=None):
    
    if save==True and save_dir == None:
        raise Exception('You tried to save without providing a save directory')
    
    scrape_list = []
    passes = 0
    
    driver.get(scrape_url)
    time.sleep(5)
    range_path = '/html/body/app-root/app-matchmaking-view/app-browse-view/div/div/div[2]/app-result-list/div[1]/div/span'
    range_str = driver.find_element_by_xpath(range_path)
    range_val = int(range_str.text)
    for k in tqdm(range(1,range_val)):
        try:
            profile_path = '/html/body/app-root/app-matchmaking-view/app-browse-view/div/div/div[2]/app-result-list/div[2]/div/app-entity-result-card[{}]'.format(k)
            profile_card = driver.find_element_by_xpath(profile_path)
            profile_card.click()
            time.sleep(2)
            name_path = '//*[@id="cdk-overlay-{}"]/app-entity-side-drawer/div/main/app-entity-profile/div/div/div/div[1]/div[1]/div/div[3]/div[1]/h2/span'.format(k)
            name_field = driver.find_element_by_xpath(name_path)
            name = name_field.text
            try:
                linkedin_path = '//*[@id="cdk-overlay-{}"]/app-entity-side-drawer/div/main/app-entity-profile/div/div/div/div[1]/div[1]/div/div[3]/div[4]/app-entity-social-links/div/a'.format(k)
                linkedin_button = driver.find_element_by_xpath(linkedin_path)
                linkedin_link = linkedin_button.get_attribute('href')
            except:
                linkedin_link = 'n/a'

            base_dict = {'name':name,'linkedin':linkedin_link}

            panel_path = '//*[@id="cdk-overlay-{}"]/app-entity-side-drawer/div/main/app-entity-profile/div/div/div/div[2]/div/app-entity-extension-list'.format(k)
            panel_field = driver.find_element_by_xpath(panel_path)
            panel_content = panel_field.text
            panel_content = panel_content.lower()
            panel_string = panel_content.strip('/n')
            panel_text = panel_string.replace('\n',' ')
            
            exit_path = '//*[@id="cdk-overlay-{}"]/app-entity-side-drawer/div/mat-toolbar/button[1]'.format(k)
            exit_button = driver.find_element_by_xpath(exit_path)
            exit_button.click()
            time.sleep(1)

            data_dict = MatchmakerExtract(panel_text,base_dict)


            scrape_list.append(data_dict)
        except:
            passes+=1


    scrape_df = pd.DataFrame(scrape_list)
    
    if save==True:
        scrape_df.to_csv(save_dir)
    print('The number of profiles missed is {}'.format(passes))
    return scrape_df