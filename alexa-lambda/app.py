# This attempts to be (more or less) the simplest possible hello world Alexa skill...

from __future__ import print_function
from botocore.vendored import requests
import json

# We'll start with a couple of globals...
CardTitlePrefix = "Greeting"

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    """
    Build a speechlet JSON representation of the title, output text,
    reprompt text & end of session
    """

    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': CardTitlePrefix + " - " + title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    """
    Build the full response JSON from the speechlet response
    """
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    session_attributes = {}
    card_title = "Hello"
    # speech_output = "Say: show me my cryptos - show me my stocks - or show me my whole porfolio"

    speech_output = "Please say: show me my cryptocurrency portfolio - show me my stocks portfolio - or show me my combined portfolio"

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "I'm sorry - I didn't understand. You should ask me to say my portfolio..."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def say_hello():
    card_title = "Greeting Message"
    greeting_string = "Adam Sucks"
    return build_response({}, build_speechlet_response(card_title, greeting_string, " ", True))

def say_Combine():
    card_title = "Combined"

    # crypto
    r = requests.get("https://2ji8y26hd8.execute-api.us-east-1.amazonaws.com/api/value/crypto/user/adam")

    temp = json.loads(r.content)
    crypto_value = float(temp['value'])

    # stocks
    r2 = requests.get("https://2ji8y26hd8.execute-api.us-east-1.amazonaws.com/api/value/portfolio/user/adam")

    temp2 = json.loads(r2.content)
    stocks_value = float(temp2['value'])

    #combined
    combined_value = int(crypto_value + stocks_value)

    greeting_string = "Your current Combined Portfolio value is: {} dollars".format(combined_value)

    # greeting_string = j['total_stock']
    return build_response({}, build_speechlet_response(card_title, greeting_string, " ", True))

def say_Crypto():
    card_title = "Crypto"

    r = requests.get("https://2ji8y26hd8.execute-api.us-east-1.amazonaws.com/api/value/crypto/user/adam")

    j = json.loads(r.content)
    greeting_string = "Your current Cryptocurrency Portfolio value is: {} dollars".format(j['value'])

    # greeting_string = j['total_stock']
    return build_response({}, build_speechlet_response(card_title, greeting_string, " ", True))

def say_Stock():
    card_title = "Stock"

    r = requests.get("https://2ji8y26hd8.execute-api.us-east-1.amazonaws.com/api/value/portfolio/user/adam")

    j = json.loads(r.content)
    greeting_string = "Your current Stocks Portfolio value is: {} dollars".format(j['value'])

    # greeting_string = j['total_stock']
    return build_response({}, build_speechlet_response(card_title, greeting_string, " ", True))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they want """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "getCombine":
        return say_Combine()
    elif intent_name == "getStock":
        return say_Stock()
        # return get_welcome_response()
    elif intent_name == "getCrypto":
        return say_Crypto()
        # return get_welcome_response()
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise  get_welcome_response()


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session. Is not called when the skill returns should_end_session=true """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])

# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])


    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
