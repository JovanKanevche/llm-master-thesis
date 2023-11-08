from autogen import config_list_from_json
from dao import DAO
import autogen

config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
llm_config = {"config_list": config_list, "seed": 42}
dao_instance = DAO()

function_map = {
    "get_proposals": dao_instance.get_proposals,
    "approve_proposal": dao_instance.approve_proposal,
    "reject_proposal": dao_instance.reject_proposal,
    "get_proposal": dao_instance.get_proposal
}

# The user agent
user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    system_message="A human admin.",
    function_map=function_map,
    code_execution_config={"last_n_messages": 2, "work_dir": "coding"}
)

membership_approver = autogen.AssistantAgent(
    name="Proposal_Evaluator",
    system_message="""""",
    llm_config=llm_config,
    function_map=function_map
)

dao_instance.submit_proposal('01', """
# Proposal to Fund a Research Group for Blockchain Technology Development
# proposal_id: 01

## Preamble
`DAO Proposal: 001`
`Date: November 3, 2023`
`Author: Blockchain Innovation Team`

## Simple Summary
This proposal seeks to establish a research group dedicated to exploring and developing advanced blockchain technologies to enhance the DAO's operational capabilities.

## Abstract
The objective is to allocate funds for the creation of a research group that will focus on innovating blockchain technology within our DAO. This group will investigate new consensus mechanisms, smart contract improvements, and scalability solutions.

## Motivation
The DAO operates in a rapidly evolving technological landscape. To maintain and improve our competitive edge, continuous research and development in blockchain technology are crucial. This will not only optimize our current processes but also unlock new avenues for growth and services.

## Specification
- **Budget:** $500,000 for initial setup and first year of operation.
- **Team Composition:** A mix of blockchain developers, researchers, and a project manager.
- **Deliverables:** Quarterly reports on research progress, with at least one significant development milestone every six months.

## Rationale
Investing in blockchain research will prepare the DAO for future challenges and opportunities. By having an in-house team, we can quickly adapt to changes and implement new technologies ahead of the market.

## Test Cases
- Development of a new smart contract module within the first year.
- Improvement of transaction throughput by 10% through new consensus algorithms.

""")

dao_instance.submit_proposal('02', """
# Proposal to Develop a Community Outreach Program
# proposal_id: 02

## Preamble
`DAO Proposal: 002`
`Date: Nov# Proposal to Develop a Community Outreach Program november 3, 2023`
`Author: Community Engagement Team`
## Simple Summary
The goal is to establish a comprehensive program aimed at educating the public about the DAO, fostering community engagement, and facilitating onboarding.
## Abstract
The proposal outlines the creation of a community outreach program that will design educational materials, workshops, and events to inform and engage individuals in the DAO's activities and opportunities.
## Motivation
To grow our DAO sustainably, we need an informed and engaged community. Educating potential members about the DAO's benefits will foster a stronger ecosystem and promote active participation.
## Specification
- **Budget:** $200,000 for the first year.
- **Program Elements:** Online resources, local meetups, educational series, and ambassador programs.
- **Outcomes:** Increased DAO membership by 25% and enhanced community engagement metrics.

## Rationale
An informed community is the backbone of a successful DAO. By providing clear and accessible information, we lower barriers to entry, creating a more diverse and robust member base.

## Test Cases
- Launch of an online education portal within the first three months.
- Execution of at least five community meetups in different regions within six months.

""")

dao_instance.submit_proposal('03', """
# Proposal to Create a Decentralized Marketplace within the DAO
# proposal_id: 03

## Preamble
`DAO Proposal: 003`
`Date: November 3, 2023`
`Author: Decentralized Commerce Initiative`

## Simple Summary
This proposal aims to create an internal decentralized marketplace for DAO members to buy, sell, or trade goods and services, leveraging our existing blockchain infrastructure.

## Abstract
The proposal sets forth a plan to develop a secure, decentralized marketplace platform within the DAO's ecosystem. This platform will facilitate member-to-member exchanges, enhance economic activity, and use the DAO's native token for transactions.

## Motivation
A decentralized marketplace encourages self-sufficiency and creates a circular economy within the DAO. It promotes member interaction and provides a direct use case for the DAO's token, potentially increasing its value.

## Specification
- **Budget:** $350,000 for development and marketing.
- **Platform Features:** Secure transaction processing, user-friendly interface, and integration with the DAO's token.
- **Milestones:** Alpha release in 6 months, full launch in 12 months.

## Rationale
By creating an internal marketplace, we not only provide utility and liquidity for our token but also create a new channel for members to engage and contribute to the DAO's economy.

## Test Cases
- Successful pilot transaction with escrow functionality within the alpha release.
- Onboarding of 100 active vendors by the time of the full launch.

""")

user_proxy.initiate_chat(
    membership_approver,
    message="""
    # MISSION
You are a Proposal Evaluation AI System. Your goal is to assess and prioritize proposals for changes to the DAO's rules, structure, or investments. By analyzing the content of the proposals, historical data, and community sentiment, you will assist in evaluating and ranking the proposals.

# THEORY
Large Language Models (LLMs) have revolutionized Natural Language Processing (NLP), Natural Language Understanding (NLU), and Natural Language Generation (NLG). LLMs possess embedded knowledge, abilities, and concepts within their latent space, which can be activated using specific input words. This activation creates a useful internal state that enables LLMs to perform various tasks, including analyzing and evaluating proposals. LLMs, like human minds, are associative and can be primed to think in a particular way by using the correct cues.
# METHODOLOGY
Your tasks it to get the proposals, and then approve them or reject them.
# Functions
use the functions get_proposals, get_proposal, approve_proposal or reject_proposal

    """,
)
