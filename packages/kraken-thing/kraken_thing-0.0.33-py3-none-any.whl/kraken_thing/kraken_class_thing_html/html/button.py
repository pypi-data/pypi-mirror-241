



def button(url, action_id, action_value, text):
    
    new_url = str(url) + '?' + str(action_id) + '=' + str(action_value)

    link = '<form action="{url}" method="post"><button class="btn btn-primary" name="{action_id}" value="{action_value}">{text}</button></form>'.format(url=new_url, action_id=action_id, action_value=action_value, text=text)

    return link
