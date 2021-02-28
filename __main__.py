import sys
import os
import yaml

import prim.parser as parser


args = parser.parse_args()

if 'func' in args:
    func = args.func
    func()

# if func:
#    func(vars(args))

