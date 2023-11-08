class DAO:
    def __init__(self):
        self.members = {}  # {address: approved}
        self.proposals = {}  # List of proposals
        self.evaluations = {}  # {proposal_id: {address: evaluation}}
        
    def apply_for_membership(self, address, resume):
        self.members[address] = {
            "approved": False,
            "resume": resume
        }  # Not approved yet

    def approve_membership(self, address):
        self.members[address]["approved"] = True
        return address + " approved please run get_unprocessed_memberships again"

    def get_unprocessed_memberships(self):
        # Returns a string of addresses with unapproved memberships, separated by commas
        return ', '.join(address for address, details in self.members.items() if not details["approved"])

    def get_resume_for_membership_approval(self, address):
        return self.members[address]["resume"]

    def submit_proposal(self, proposal_id, proposal):
        self.proposals[proposal_id] = proposal  # Add proposal to the list

    def get_proposals(self):
        return ', '.join(self.proposals.keys())  # Return proposal IDs as a comma-separated string
    
    def get_proposal(self, proposal_id):
        return self.proposals.get(proposal_id, None)
    
    def approve_proposal(self, proposal_id):
        if proposal_id not in self.evaluations:
            self.evaluations[proposal_id] = False

        self.evaluations[proposal_id] = False
        return "Proposal Approval recorded; run get_proposals again;"
    
    def reject_proposal(self, proposal_id):
        if proposal_id not in self.evaluations:
            self.evaluations[proposal_id] = False

        self.evaluations[proposal_id] = True
        return "Proposal Rejection recorded; run get_proposals again;"
     