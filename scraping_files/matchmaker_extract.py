from keyword_match import KeyWordMatch

def MatchmakerExtract(trial_text,base_dict):
    
    location = KeyWordMatch('location_on','business',trial_text)
    
    description = KeyWordMatch('short description of yourself','your profession',trial_text)
    
    profession = KeyWordMatch('your profession','people i would',trial_text)
    
    people_meet = KeyWordMatch('like to meet','meeting themes',trial_text)
    
    areas_interest = KeyWordMatch('areas of interest','this is the end of the description',trial_text)
    
    industry_investment = KeyWordMatch('what industries do you invest in','do you invest in',trial_text)
    
    investment_turnover = KeyWordMatch('turnover stage of the startups you invest in','primary',trial_text)
    
    investment_size = KeyWordMatch('what is the size range of your typical investment in startups','what is the turnover stage', trial_text)
    
    investment_region = KeyWordMatch('investment regions','matchmaking profile short', trial_text)
    
    fund_size = KeyWordMatch('general fund size','what startup stages is your fund',trial_text)
    
    startup_stage = KeyWordMatch('startup stages is your fund focusing on','this is the end of the description',trial_text)
    
    
    data_dict = base_dict
    data_dict.update({'location':location,'description':description,'profession':profession,'areas of interest':areas_interest,'people to meet':people_meet,
                      'investment industries':industry_investment,'investment size':investment_size,'investee company turnover':investment_turnover,'investment regions':investment_region,
                     'fund size':fund_size,'startup stage':startup_stage})
    
    return data_dict