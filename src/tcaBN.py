# This script generates a Bayesian Network for Thyroid cancer diagnosis.
# It uses pybn (lowercase). pybn is described at http://hackl.github.io/pybn/
# pybn can be installed into this directory with
#   git clone git://github.com/pbchase/pybn.git
# Copy this file the just-cloned directory, change directory and run the copied file.
#   cp tcaBN.py pybn
#   cd pybn
#   python tcaBN.py

from pybn import *

def main():

    def printBeliefs(nodes):
        beliefs = [ (x, x.getBeliefs()) for x in nodes ]
        for (node, probs) in beliefs:
            print node, probs

    tcancer = Network("Thyroid Cancer")

    # Add nodes
    mc = Node("mc")
    im = Node("im")
    he = Node("he")
    #pv = Node("Peripheral vascularity")
    #rs = Node("Round shape")

    ca = Node("ca")
    op = Node("op")
    kw = Node("kw")

    # enumerate those nodes
    nodes = [mc, im, he, ca, op, kw]

    # Add outcomes for each node
    [ x.addOutcomes(['yes', 'no']) for x in nodes]

    # Add edges between nodes
    arc_mc_ca = Arc(mc,ca)
    arc_im_ca = Arc(im,ca)
    arc_he_ca = Arc(he,ca)
    # arc_pv_ca = Arc(pv,ca)
    # arc_rs_ca = Arc(rs,ca)

    arc_ca_op = Arc(ca,op)
    arc_ca_kw = Arc(ca,kw)

    # set probabilities for nodes with no parents
    # from Kim et al, 2002, "New Sonographic Criteria for Recommending Fine-Needle Aspiration Biopsy of Nonpalpable Solid Nodules of the Thyroid"
    # 155 non-palpable nodules were found in patients with no outward synptoms of thyroid CA.
    mc.setProbabilities([0.28,0.72])
    im.setProbabilities([0.35,0.65])
    he.setProbabilities([0.15,0.85])
    # pv.setProbabilities([0.12,0.88])
    # rs.setProbabilities([,])

    # set probabilities for nodes with parents
    # These values are made up from but not entirely random
    # They are attempts to estimate what real values might be in a clinical situation
    ca.setProbabilities([0.88,0.12,0.8,0.2,0.6,0.4,0.7,0.3,0.5,0.5,0.6,0.4,0.3,0.7,0.1,0.9])
    op.setProbabilities([0.95,0.05,0.10,0.90])
    kw.setProbabilities([0.01,0.99,0.30,0.70])

    # Add nodes to the network
    tcancer.addNodes(nodes)

    # save the file that defines the network
    tcancer.writeFile('tcancer_network.xsdl')

    # compute the beliefs of the network
    tcancer.computeBeliefs()

    printBeliefs(nodes)
    print ""

    # state some evidence and re-examine the beliefs
    tcancer.reset()
    tcancer.setEvidence('mc', 1)
    tcancer.computeBeliefs()
    printBeliefs(nodes)
    print ""

    # state some evidence and re-examine the beliefs
    tcancer.reset()
    tcancer.setEvidence('mc', 1)
    tcancer.setEvidence('im', 1)
    tcancer.computeBeliefs()
    printBeliefs(nodes)
    print ""


if __name__ == '__main__':
  main()

