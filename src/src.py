"""
Simple Python Lambda function providing helpful tips for dog owners in Richmond, Va.
Intents supported:
    About
    Contact
    Upcoming

"""

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

import random
# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(card_title, card_content, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': output
        },
        'card': {
            'type': 'Simple',
            'title': card_title,
            'content': card_content
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
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- functions to implement the intents ------------------

def about(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True

    card_output = "In addition to the more than 35 publications that VistaGraphics publishes regularly, we also offer our clients custom publishing services."
    speech_output = "<speak>We excel at making connections. Vista Graphics is a leader in quality publications, targeted digital marketing and event management services. In addition to the more than 35 publications that Vista Graphics publishes regularly, they also offer our clients custom publishing services. Whether it’s for a Destination Marketing Organization, a nonprofit organization, or a national corporation, VistaGraphics, Inc. provides agency-quality design and production to meet your specific needs. No job is too large, Nor, too small.</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("About", card_output, speech_output, reprompt_text, should_end_session))

def contact(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True

    card_output = "WEBSITE: VistaGraphicsInc.com | PHONE: (757) 422-8979 | EMAIL: info@vgnet.com"
    speech_output = "<speak>Vista Graphics Inc is located at 1-2-6-4 Perimeter Parkway, in Virginia Beach, VA. <break time=\"0.5s\"/> For information about our Publishing Services, Advertising Opportunities, Digital Services, Event Services, or for general inquiries, you can reach Vista Graphics by phone at. <break time=\"0.25s\"/> 7-5-7. 4-2-2. 8-9-7-9. You can also check out their website at Vista Graphics inc dot com.</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Contact Details", card_output, speech_output, reprompt_text, should_end_session))

def services(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True

    card_output = "Services offered by VistaGraphics: Publishing, Digital Marketing, Vista Promos Division, Events & Ticketing."
    speech_output = "<speak>Vista Graphics offers an array of services to help your business or event. Ask me about a service and I'll happily tell you a little more about that offering. For example, you can say <break time=\"0.25s\"/> Publishing. Digital Marketing. Promotions. Events <break time=\"0.25s\"/> or Ticketing.</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Services", card_output, speech_output, reprompt_text, should_end_session))


services_list = [
    'We now account for over 40 titles annually in the hospitality, lifestyle and specialized genres. With each publication, quality is the focus. We believe that the quality of the magazine affects the quality and receptiveness of the message. Print creates an emotional connection and builds relationships. A 2017 Marketing Sherpa study found that of all media, US internet users trust print ads the most.',
    'With an ever growing need for dedicated Internet service solutions, Vista Internet Marketing Solutions, Inc. was born to answer that call. As a division of VistaGraphics, Inc. your company will receive the same top quality care and service from our team of highly skilled professionals that our clients have enjoyed for over 30 years. We have built a solid team of designers, developers, SEO and marketing specialists.',
    'Are you looking for creative ways to market and brand your company or business? VistaGraphics has launched a new division for promotional products called VistaPromos. We provide a full spectrum of promotional products which enhance your competitive presence, brand image and exposure to your target audience. Every business should incorporate promotional products into their ad campaigns.',
    'We manage and promote dozens of events each year. Through sponsorships, these events now provide an additional platform for our clients to grow and extend their brand. We also offer clients a method for selling tickets and promoting their events, via our online ticket portals through <break time=\"0.25s\"/> Cova Ticks <break time=\"0.25s\"/> and Hill-City Ticks. These platforms are competitively priced, user friendly and customizable to fit the needs of each event.'
]

def publishing_services(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True
    
    card_output = "VistaGraphics publishes over 40 titles annually in the hospitality, lifestyle and specialized genres. With each publication, quality is the focus."
    speech_output = "<speak>A little about our publishing services <break time=\"0.25s\"/>. " + services_list[0] + " </speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Publishing Services", card_output, speech_output, reprompt_text, should_end_session))


def digital_marketing(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True
    
    card_output = "With an ever growing need for dedicated Internet service solutions, Vista Internet Marketing Solutions, Inc. was born to answer that call."
    speech_output = "<speak>A little about our digital marketing <break time=\"0.25s\"/>. " + services_list[1] + " </speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Digital Marketing", card_output, speech_output, reprompt_text, should_end_session))


def vista_promos_div(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True
    
    card_output = "VistaGraphics has launched a new division for promotional products called VistaPromos to help market and brand your company."
    speech_output = "<speak>A little about our Vista Promos Division <break time=\"0.25s\"/>. " + services_list[2] + " </speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Vista Promos Division", card_output, speech_output, reprompt_text, should_end_session))


def events_ticketing_services(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True
    
    card_output = "Check out CoVaTIX.com and HillCityTIX.com | We manage and promote dozens of events each year and offer clients a method for selling tickets and promoting events."
    speech_output = "<speak>Through our Events and Ticketing Services <break time=\"0.25s\"/> " + services_list[3] + " </speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Events and Ticketing Services", card_output, speech_output, reprompt_text, should_end_session))


# List of example testimonials to return when testimonials() is called
testimonials_list = [
    "The app has been a game changer for the Zoo. We have been able to achieve a big green initiative by eliminating paper maps completely. Plus, we have expanded our conservation and educational messaging to people of all ages through the technology. Says Greg Bockheim, Virginia Zoo's Executive Director.",
    "We just wanted to thank you again for having our winery there this year.  You did a fabulous job!!! Everyone was so helpful and professional. Says Pamela Cowdrey, from Castle Glen Estates Farm and Winery.",
    "The bridal show was absolutely wonderful! I always take approximately 400-500 samples to a bridal show and I ran out!!! Says Alice Cooke, from Creations From the Heart.",
    "The Visitor's Guide has been instrumental in success through targeted and broad marketing, to ensure our brand and products reach our potential customers. Says David Williams, from Donutz On A Stick.",
    "It reaches and attracts the right customers for our business's growth. Also, the creative resources make this truly a marketing partnership! Says, Atoosa Nikzad, from Changes Hairstyling and City Spa.",
    "Visitors Guide has given me the best response of any media I've advertised in! My coupon redemption was on point!. Says Sam Esleek, from the Sauce Shoppe."
    ]

def testimonials(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True
    
    card_output = "Sweet Words From Our Clients"
    speech_output = "<speak>Here is what someone said about Vista Graphics " + random.choice(testimonials_list) + " </speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Testimonials", card_output, speech_output, reprompt_text, should_end_session))


def stop(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True
    
    card_output = "Have a nice day!"
    speech_output = "<speak>Thank you for asking about Vista Graphics Inc. Have a nice day!</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Session Ended", card_output, speech_output, reprompt_text, should_end_session))




def get_help(intent, session):
    """ Called when the user asks for help """
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = False
    
    card_output = "You can ask Vista Graphics: About, Contact, Testimonials, or Services."
    speech_output = "<speak>You can ask me things like, About, Contact, Testimonials, or Services.</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Things to Ask", card_output, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for checking out the Vista Graphics Alexa Skill."
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

# --------------- Primary Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    logger.info("on_session_started requestId=" + session_started_request['requestId'] +
                ", sessionId=" + session['sessionId'])
                

def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    logger.info("on_launch requestId=" + launch_request['requestId'] +
                ", sessionId=" + session['sessionId'])
    
    # Dispatch to skill's launch
    return build_response({},build_speechlet_response(
        "Vista Graphics, Inc.", "Welcome to the Amazon Alexa skill, Vista Graphics!", "<speak>Welcome to the Amazon Alexa skill, Vista Graphics. I will give the 4-1-1 on Vista Graphics Inc. To learn more, just drop me a line by asking me About, Contact, or say. Alexa, ask Vista Graphics for help.</speak>","",False))


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    logger.info("on_intent requestId=" + intent_request['requestId'] +
                ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to skill's intent handlers

    if intent_name == "About":
        return about(intent, session)
    elif intent_name == "Contact":
        return contact(intent, session)
    elif intent_name == "Services":
        return services(intent, session)
    elif intent_name == "ServicePublishing":
        return publishing_services(intent, session)
    elif intent_name == "ServiceDigital":
        return digital_marketing(intent, session)
    elif intent_name == "ServicePromos":
        return vista_promos_div(intent, session)
    elif intent_name == "ServiceEventsTickets":
        return events_ticketing_services(intent, session)
    elif intent_name == "Testimonials":
        return testimonials(intent, session)
    elif intent_name == "Stop":
        return stop(intent, session)
    elif intent_name == "GetHelp":
        return get_help(intent, session)
#    elif intent_name == "AMAZON.HelpIntent":
#        return get_help()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")

def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    logger.info("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    else:
        return on_session_ended(event['request'], event['session'])