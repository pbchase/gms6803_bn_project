#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
import logging
import logging.handlers

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s]: %(levelname)s: %(message)s')

def BN_net(RS = 0, MC = 0, CA = 0, PV = 0, HE = 0):

    #The probability of being a malignant nodule
    P_mal = 0.37 * MC + 0.22 * CA + 0.63 * PV + 0.585 * HE + 0.37 * RS
    #The probability of being a benign nodule
    P_ben = 1 - P_mal

    return P_mal, P_ben

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-r', '--rs', help="define the value of the RS;", type = int, dest = 'rs', required=True)
    parser.add_argument(
        '-m', '--mc', help="define the value of the MC;", type = int, dest = 'mc', required=True)
    parser.add_argument(
        '-c', '--ca', help="define the value of the CA;", type = int, dest = 'ca', required=True)
    parser.add_argument(
        '-p', '--pv', help="define the value of the PV;", type = int, dest = 'pv', required=True)
    parser.add_argument(
        '-e', '--he', help="define the value of the HE;", type = int, dest = 'he', required=True)

    args = parser.parse_args()

    P_mal, P_ben = BN_net(args.rs, args.mc, args.ca, args.pv, args.he)

    logger.info('The probability of being a malignant nodule is %f' %P_mal)
    logger.info('The probability of being a benign nodule is %f' %P_ben)