import hivnetworkcsv

if ('arguments' in globals()):
    # set command line arguments, from javascript
    hivnetworkcsv.sys.argv = arguments.split()
    hivnetworkcsv.main()