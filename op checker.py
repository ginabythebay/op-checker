#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def output(txt):
    app = adsk.core.Application.get()
    ui  = app.userInterface
    ui.palettes.itemById('TextCommands').writeText(txt)

def fmtAxis(p, name):
    n=p.itemByName(name).expression
    return f'{n:7.6}'

def logSetup(setup):
    p = setup.parameters

    output('')
    output(f'setup {setup.name}')
    output(f'    axis \tstock high \tstock low')
    output(f'    Z    \t{fmtAxis(p, "stockZHigh")}\t\t{fmtAxis(p, "stockZLow")}')
    output(f'    X    \t{fmtAxis(p, "stockXHigh")}\t\t{fmtAxis(p, "stockXLow")}')
    output(f'    Y    \t{fmtAxis(p, "stockYHigh")}\t\t{fmtAxis(p, "stockYLow")}')

def run(context):
    ui = None
    try:
        # Get the application.
        app = adsk.core.Application.get()
        ui  = app.userInterface

        # Get the active document.
        doc = app.activeDocument

        # Get the products collection on the active document.
        products = doc.products

        # Get the CAM product.
        product = products.itemByProductType('CAMProductType')

        # Check if the document has a CAMProductType. It will not if there are no CAM operations in it.
        if product == None:
            ui.messageBox('There are no CAM operations in the active document')
            return

        # Cast the CAM product to a CAM object (a subtype of product).
        cam = adsk.cam.CAM.cast(product)

        output(f'**************************')
        for setup in cam.setups:
            logSetup(setup)
            #for prm in setup.parameters:
            #    print('{} : {}'.format(prm.name, prm.expression))

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def stop(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        # ui.messageBox('Stop params')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
