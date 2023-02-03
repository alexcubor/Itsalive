import nuke


def CloseAllProperties():
    # for each node, even the ones in groups
    for n in nuke.allNodes(recurseGroups=True):
        # hide the control panel
        n.hideControlPanel()

    nuke.root().hideControlPanel()
