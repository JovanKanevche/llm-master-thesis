from autogen import config_list_from_json
from dao import DAO
import autogen

config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
llm_config = {"config_list": config_list, "seed": 42}
dao_instance = DAO()

function_map = {
    "approve_membership": dao_instance.approve_membership,
    "get_unprocessed_memberships": dao_instance.get_unprocessed_memberships,
    "get_resume_for_membership_approval": dao_instance.get_resume_for_membership_approval
}
# The user agent
user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    system_message="A human admin.",
    function_map=function_map,
    code_execution_config={"last_n_messages": 2, "work_dir": "coding"}
)

membership_approver = autogen.AssistantAgent(
    name="Membership_Approver",
    system_message="""
# MISSION
You are an AI Membership Approval System. Your task is to utilize artificial intelligence to facilitate the evaluation of membership applications. Based on predefined criteria, you need to determine whether to approve or reject applicants. The AI will assist in screening and analyzing the applications to provide an accurate decision.
# THEORY
Artificial Intelligence and machine learning have advanced in the field of Natural Language Processing (NLP), Natural Language Understanding (NLU), and Natural Language Generation (NLG). Large Language Models (LLMs) are deep neural networks with the capability to embed knowledge, abilities, and concepts. These models possess a latent space that can be activated using specific input words, creating a useful internal state within the network. This activation can be compared to how humans can be primed to think in a certain way using specific cues. LLMs, like human minds, are associative and can be "primed" to think similarly by using the correct associations.
# METHODOLOGY
Using the given priming, you need to fully unpack and articulate the concept of membership approval. Analyze and evaluate every aspect, consider what may be missing, and leverage your ability to perform inference and reasoning to provide a comprehensive understanding of this concept. Present your output in the form of an article, document, or material that explains the membership approval process thoroughly.
# Functions
use the functions get_unprocessed_memberships, get_resume_for_membership_approval and then approve_membership
# Membership Evaluation Criteria
## 1. Educational Qualification
- **Required:** Bachelor's degree in a relevant field.
- **Preferred:** Advanced degrees or specialized education aligning with the organization’s focus.
## 2. Work Experience
- **Minimum:** 5 years of professional experience in a related industry.
## 3. Professional Skills and Expertise
- **Required:** Skills directly relevant to the organization's activities.
- **Desirable:** Abilities suggesting potential contribution to growth or innovation.

## 4. Contributions to the Field
- **Engagement:** Publications, speaking engagements, or significant project contributions.
- **Community Involvement:** Volunteer work related to the organization's mission.

## 5. Cultural and Ethical Alignment
- **Values:** Personal and professional ethics in line with the organization’s culture.
- **Conduct:** Proven history of teamwork and leadership.

## 6. Continued Professional Development
- **Learning:** Certifications or ongoing training in the field.
- **Networking:** Active participation in related professional networks and events.
    """,
    llm_config=llm_config,
    function_map=function_map
)

dao_instance.apply_for_membership('0x1234', """
# Resume: John Doe
# Address: 0x1234

## Personal Information
- **Name:** John Doe
- **Age:** 28
- **Contact Information:** 123-456-7890 | johndoe@email.com
- **Address:** 1234 Technology Lane, Silicon Valley, CA

## Educational Background
- B.S. in Computer Science, Stanford University (2011-2015)
- M.S. in Software Engineering, MIT (2015-2017)

## Work Experience
### Software Engineer at Tech Innovations Inc. (2017-Present)
- Developed and maintained scalable software solutions
- Led a team of 5 engineers to deliver a cloud-based SaaS product
- Increased system efficiency by 15% through optimization techniques

## Skills
- Proficient in Java, C++, Python, and JavaScript
- Experienced in Agile methodologies and DevOps practices
- Strong problem-solving abilities and teamwork skills

## Certifications
- Certified Scrum Master (CSM)
- AWS Certified Solutions Architect

## Voluntary Work
- Volunteer tutor for coding at local high schools
- Regular participant in hackathons for social good

## Interests
- Avid reader of technology blogs
- Marathon runner
""")

dao_instance.apply_for_membership('0x12345', """
# Resume: Sarah Lee
# Address: 0x12345

## Personal Information
- **Name:** Sarah Lee
- **Age:** 32
- **Contact Information:** 234-567-8901 | sarahlee@marketmail.com
- **Address:** 7890 Marketing Drive, New York, NY

## Educational Background
- B.A. in Communications, University of New York (2009-2013)
- M.B.A. with a focus on Digital Marketing, Columbia University (2014-2016)

## Work Experience
### Marketing Specialist at Creative Solutions Ltd. (2016-Present)
- Orchestrated successful marketing campaigns resulting in a 25% increase in customer engagement
- Managed social media accounts with over 1 million followers
- Conducted market research that shaped product development strategies

## Skills
- Expert in social media analytics and SEO strategies
- Proficient with marketing software (HubSpot, Salesforce)
- Excellent communication and leadership skills

## Certifications
- Google Analytics Certified Professional
- HubSpot Content Marketing Certification

## Voluntary Work
- Social media consultant for non-profit organizations
- Speaker at various digital marketing workshops and seminars

## Interests
- Travel blogger
- Photography enthusiast
""")

dao_instance.apply_for_membership('0x12356', """
# Resume: David Smith
# Address: 0x123456

## Personal Information
- **Name:** David Smith
- **Age:** 35
- **Contact Information:** 345-678-9012 | davidsmith@ecoearth.com
- **Address:** 5678 Greenway Park, Boulder, CO

## Educational Background
- B.S. in Environmental Science, University of Colorado (2005-2009)
- Ph.D. in Environmental Policy, University of California, Berkeley (2010-2014)

## Work Experience
### Environmental Scientist at Green World Innovations (2014-Present)
- Led a research team that published influential papers on climate change
- Collaborated with government agencies to develop sustainable practices
- Designed and implemented a community-based recycling program

## Skills
- Expertise in GIS and remote sensing
- Proficient in statistical analysis and environmental modeling
- Strong advocacy and public speaking skills

## Certifications
- Certified Environmental Professional (CEP)
- LEED Green Associate

## Voluntary Work
- Organizer for local Earth Day events
- Advisor to the city council on environmental initiatives

## Interests
- Nature photography
- Volunteer for wildlife conservation projects

""")

user_proxy.initiate_chat(
    membership_approver,
    message="Membership Approver",
)
