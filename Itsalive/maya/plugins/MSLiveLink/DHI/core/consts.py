from collections import OrderedDict

SCALE = 1.0
SCALE_PIVOT = [0.0, 0.0, 0.0]
ORIENT_X = [0.0, 90.0, 0.0]
ORIENT_Y = [0.0, 0.0, 0.0]
ORIENT_Z = [90.0, 0.0, 0.0]

TRANSLATE_FACTOR = [0.0, 0.0, 2.0]

ADAPT_MESH_NAMES = ["head_lod0_mesh",
"eyeshell_lod0_mesh",
"eyelashes_lod0_mesh",
"eyelashesShadow_lod0_mesh",
"eyeEdge_lod0_mesh"]

MESH_NAMES = ["head_lod0_mesh",
"teeth_lod0_mesh",
"saliva_lod0_mesh",
"eyeLeft_lod0_mesh",
"eyeRight_lod0_mesh",
"eyeshell_lod0_mesh",
"eyelashes_lod0_mesh",
"eyelashesShadow_lod0_mesh",
"eyeEdge_lod0_mesh",
"cartilage_lod0_mesh",
"head_lod1_mesh",
"teeth_lod1_mesh",
"saliva_lod1_mesh",
"eyeLeft_lod1_mesh",
"eyeRight_lod1_mesh",
"eyeshell_lod1_mesh",
"eyelashes_lod1_mesh",
"eyelashesShadow_lod1_mesh",
"eyeEdge_lod1_mesh",
"cartilage_lod1_mesh",
"head_lod2_mesh",
"teeth_lod2_mesh",
"saliva_lod2_mesh",
"eyeLeft_lod2_mesh",
"eyeRight_lod2_mesh",
"eyeshell_lod2_mesh",
"eyelashes_lod2_mesh",
"eyeEdge_lod2_mesh",
"lashesMHC_lod2_mesh",
"head_lod3_mesh",
"teeth_lod3_mesh",
"eyeLeft_lod3_mesh",
"eyeRight_lod3_mesh",
"eyeshell_lod3_mesh",
"eyelashes_lod3_mesh",
"eyeEdge_lod3_mesh",
"lashesMHC_lod3_mesh",
"head_lod4_mesh",
"teeth_lod4_mesh",
"eyeLeft_lod4_mesh",
"eyeRight_lod4_mesh",
"eyeshell_lod4_mesh",
"head_lod5_mesh",
"teeth_lod5_mesh",
"eyeLeft_lod5_mesh",
"eyeRight_lod5_mesh",
"head_lod6_mesh",
"teeth_lod6_mesh",
"eyeLeft_lod6_mesh",
"eyeRight_lod6_mesh",
"head_lod7_mesh",
"teeth_lod7_mesh",
"eyeLeft_lod7_mesh",
"eyeRight_lod7_mesh"
]

GUI_NAMES = ["GRP_faceGUI"]

GUI_TRANSLATIONS = {
     "f_med": None,
     "f_srt": [-9.98377799988e-07, -7.43420410156, -8.58306884766e-06],
     "f_tal": [0.0, 8.09687805176, 0.0],
     "m_med": [-1.98682149066e-08, -3.53102281359, 0.262324757046],
     "m_srt": [-6.02503617603e-06, -11.7652910021, 0.262353367276],
     "m_tal": [-1.98682149066e-08, 3.62467787001, 0.26234096951]
}

GUI_SCALES = {
 "f_med": None,
 "f_srt": None,
 "f_tal": None,
 "m_med": 1.11111111111,
 "m_srt": 1.11111111111,
 "m_tal": 1.11111111111
}

CONTROL_NAMES = ["GRP_C_eyesAim", "LOC_C_eyeDriver"]

ADD_CONTROL_ATTRIBUTES_TO_ROOT = True
ADD_WM_ATTRIBUTES_TO_ROOT = True
RENAME_BLENDSHAPES = True

NECK_MESHES = ["head_lod0_mesh",
"eyeshell_lod0_mesh",
"eyelashes_lod0_mesh",
"eyelashesShadow_lod0_mesh",
"eyeEdge_lod0_mesh"]

FACIAL_ROOT_JOINTS = ["FACIAL_C_FacialRoot", "FACIAL_C_Neck1Root", "FACIAL_C_Neck2Root"]
NECK_JOINTS = ["spine_04",
"clavicle_l",
"clavicle_r",
"upperarm_out_l",
"upperarm_fwd_l",
"upperarm_bck_l",
"neck_01",
"neck_02",
"head",
"upperarm_in_l",
"clavicle_out_l",
"clavicle_pec_l",
"clavicle_scap_l",
"clavicle_pec_r",
"clavicle_out_r",
"clavicle_scap_r",
"upperarm_bck_r",
"upperarm_in_r",
"upperarm_fwd_r",
"upperarm_out_r",
"spine_04_latissimus_l",
"spine_04_latissimus_r"]

ROOT_JOINT_NAME = "root"

CONTROL_MAP = OrderedDict([(u'CTRL_expressions.browDownL', (u'CTRL_expressions_browDownL', 0.0, 1.0)),
 (u'CTRL_expressions.browDownR', (u'CTRL_expressions_browDownR', 0.0, 1.0)),
 (u'CTRL_expressions.browLateralL', (u'CTRL_expressions_browLateralL', 0.0, 1.0)),
 (u'CTRL_expressions.browLateralR', (u'CTRL_expressions_browLateralR', 0.0, 1.0)),
 (u'CTRL_expressions.browRaiseInL', (u'CTRL_expressions_browRaiseInL', 0.0, 1.0)),
 (u'CTRL_expressions.browRaiseInR', (u'CTRL_expressions_browRaiseInR', 0.0, 1.0)),
 (u'CTRL_expressions.browRaiseOuterL', (u'CTRL_expressions_browRaiseOuterL', 0.0, 1.0)),
 (u'CTRL_expressions.browRaiseOuterR', (u'CTRL_expressions_browRaiseOuterR', 0.0, 1.0)),
 (u'CTRL_expressions.earUpL', (u'CTRL_expressions_earUpL', 0.0, 1.0)),
 (u'CTRL_expressions.earUpR', (u'CTRL_expressions_earUpR', 0.0, 1.0)),
 (u'CTRL_expressions.eyeBlinkL', (u'CTRL_expressions_eyeBlinkL', 0.0, 1.0)),
 (u'CTRL_expressions.eyeBlinkR', (u'CTRL_expressions_eyeBlinkR', 0.0, 1.0)),
 (u'CTRL_expressions.eyeLidPressL', (u'CTRL_expressions_eyeLidPressL', 0.0, 1.0)),
 (u'CTRL_expressions.eyeLidPressR', (u'CTRL_expressions_eyeLidPressR', 0.0, 1.0)),
 (u'CTRL_expressions.eyeWidenL', (u'CTRL_expressions_eyeWidenL', 0.0, 1.0)),
 (u'CTRL_expressions.eyeWidenR', (u'CTRL_expressions_eyeWidenR', 0.0, 1.0)),
 (u'CTRL_expressions.eyeSquintInnerL', (u'CTRL_expressions_eyeSquintInnerL', 0.0, 1.0)),
 (u'CTRL_expressions.eyeSquintInnerR', (u'CTRL_expressions_eyeSquintInnerR', 0.0, 1.0)),
 (u'CTRL_expressions.eyeCheekRaiseL', (u'CTRL_expressions_eyeCheekRaiseL', 0.0, 1.0)),
 (u'CTRL_expressions.eyeCheekRaiseR', (u'CTRL_expressions_eyeCheekRaiseR', 0.0, 1.0)),
 (u'CTRL_expressions.eyeFaceScrunchL', (u'CTRL_expressions_eyeFaceScrunchL', 0.0, 1.0)),
 (u'CTRL_expressions.eyeFaceScrunchR', (u'CTRL_expressions_eyeFaceScrunchR', 0.0, 1.0)),
 (u'CTRL_expressions.eyeUpperLidUpL', (u'CTRL_expressions_eyeUpperLidUpL', 0.0, 1.0)),
 (u'CTRL_expressions.eyeUpperLidUpR', (u'CTRL_expressions_eyeUpperLidUpR', 0.0, 1.0)),
 (u'CTRL_expressions.eyeRelaxL', (u'CTRL_expressions_eyeRelaxL', 0.0, 1.0)),
 (u'CTRL_expressions.eyeRelaxR', (u'CTRL_expressions_eyeRelaxR', 0.0, 1.0)),
 (u'CTRL_expressions.eyeLowerLidUpL', (u'CTRL_expressions_eyeLowerLidUpL', 0.0, 1.0)),
 (u'CTRL_expressions.eyeLowerLidUpR', (u'CTRL_expressions_eyeLowerLidUpR', 0.0, 1.0)),
 (u'CTRL_expressions.eyeLowerLidDownL', (u'CTRL_expressions_eyeLowerLidDownL', 0.0, 1.0)),
 (u'CTRL_expressions.eyeLowerLidDownR', (u'CTRL_expressions_eyeLowerLidDownR', 0.0, 1.0)),
 (u'CTRL_expressions.eyeLookUpL', (u'CTRL_expressions_eyeLookUpL', 0.0, 1.0)),
 (u'CTRL_expressions.eyeLookUpR', (u'CTRL_expressions_eyeLookUpR', 0.0, 1.0)),
 (u'CTRL_expressions.eyeLookDownL', (u'CTRL_expressions_eyeLookDownL', 0.0, 1.0)),
 (u'CTRL_expressions.eyeLookDownR', (u'CTRL_expressions_eyeLookDownR', 0.0, 1.0)),
 (u'CTRL_expressions.eyeLookLeftL', (u'CTRL_expressions_eyeLookLeftL', 0.0, 1.0)),
 (u'CTRL_expressions.eyeLookLeftR', (u'CTRL_expressions_eyeLookLeftR', 0.0, 1.0)),
 (u'CTRL_expressions.eyeLookRightL', (u'CTRL_expressions_eyeLookRightL', 0.0, 1.0)),
 (u'CTRL_expressions.eyeLookRightR', (u'CTRL_expressions_eyeLookRightR', 0.0, 1.0)),
 (u'CTRL_expressions.eyePupilWideL', (u'CTRL_expressions_eyePupilWideL', 0.0, 1.0)),
 (u'CTRL_expressions.eyePupilWideR', (u'CTRL_expressions_eyePupilWideR', 0.0, 1.0)),
 (u'CTRL_expressions.eyePupilNarrowL', (u'CTRL_expressions_eyePupilNarrowL', 0.0, 1.0)),
 (u'CTRL_expressions.eyePupilNarrowR', (u'CTRL_expressions_eyePupilNarrowR', 0.0, 1.0)),
 (u'CTRL_expressions.eyeParallelLookDirection', (u'CTRL_expressions_eyeParallelLookDirection', 0.0, 1.0)),
 (u'CTRL_expressions.eyelashesUpINL', (u'CTRL_expressions_eyelashesUpINL', 0.0, 1.0)),
 (u'CTRL_expressions.eyelashesUpINR', (u'CTRL_expressions_eyelashesUpINR', 0.0, 1.0)),
 (u'CTRL_expressions.eyelashesUpOUTL', (u'CTRL_expressions_eyelashesUpOUTL', 0.0, 1.0)),
 (u'CTRL_expressions.eyelashesUpOUTR', (u'CTRL_expressions_eyelashesUpOUTR', 0.0, 1.0)),
 (u'CTRL_expressions.eyelashesDownINL', (u'CTRL_expressions_eyelashesDownINL', 0.0, 1.0)),
 (u'CTRL_expressions.eyelashesDownINR', (u'CTRL_expressions_eyelashesDownINR', 0.0, 1.0)),
 (u'CTRL_expressions.eyelashesDownOUTL', (u'CTRL_expressions_eyelashesDownOUTL', 0.0, 1.0)),
 (u'CTRL_expressions.eyelashesDownOUTR', (u'CTRL_expressions_eyelashesDownOUTR', 0.0, 1.0)),
 (u'CTRL_expressions.noseWrinkleL', (u'CTRL_expressions_noseWrinkleL', 0.0, 1.0)),
 (u'CTRL_expressions.noseWrinkleR', (u'CTRL_expressions_noseWrinkleR', 0.0, 1.0)),
 (u'CTRL_expressions.noseWrinkleUpperL', (u'CTRL_expressions_noseWrinkleUpperL', 0.0, 1.0)),
 (u'CTRL_expressions.noseWrinkleUpperR', (u'CTRL_expressions_noseWrinkleUpperR', 0.0, 1.0)),
 (u'CTRL_expressions.noseNostrilDepressL', (u'CTRL_expressions_noseNostrilDepressL', 0.0, 1.0)),
 (u'CTRL_expressions.noseNostrilDepressR', (u'CTRL_expressions_noseNostrilDepressR', 0.0, 1.0)),
 (u'CTRL_expressions.noseNostrilDilateL', (u'CTRL_expressions_noseNostrilDilateL', 0.0, 1.0)),
 (u'CTRL_expressions.noseNostrilDilateR', (u'CTRL_expressions_noseNostrilDilateR', 0.0, 1.0)),
 (u'CTRL_expressions.noseNostrilCompressL', (u'CTRL_expressions_noseNostrilCompressL', 0.0, 1.0)),
 (u'CTRL_expressions.noseNostrilCompressR', (u'CTRL_expressions_noseNostrilCompressR', 0.0, 1.0)),
 (u'CTRL_expressions.noseNasolabialDeepenL', (u'CTRL_expressions_noseNasolabialDeepenL', 0.0, 1.0)),
 (u'CTRL_expressions.noseNasolabialDeepenR', (u'CTRL_expressions_noseNasolabialDeepenR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthCheekSuckL', (u'CTRL_expressions_mouthCheekSuckL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthCheekSuckR', (u'CTRL_expressions_mouthCheekSuckR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthCheekBlowL', (u'CTRL_expressions_mouthCheekBlowL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthCheekBlowR', (u'CTRL_expressions_mouthCheekBlowR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsBlowL', (u'CTRL_expressions_mouthLipsBlowL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsBlowR', (u'CTRL_expressions_mouthLipsBlowR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLeft', (u'CTRL_expressions_mouthLeft', 0.0, 1.0)),
 (u'CTRL_expressions.mouthRight', (u'CTRL_expressions_mouthRight', 0.0, 1.0)),
 (u'CTRL_expressions.mouthUp', (u'CTRL_expressions_mouthUp', 0.0, 1.0)),
 (u'CTRL_expressions.mouthDown', (u'CTRL_expressions_mouthDown', 0.0, 1.0)),
 (u'CTRL_expressions.mouthUpperLipRaiseL', (u'CTRL_expressions_mouthUpperLipRaiseL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthUpperLipRaiseR', (u'CTRL_expressions_mouthUpperLipRaiseR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLowerLipDepressL', (u'CTRL_expressions_mouthLowerLipDepressL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLowerLipDepressR', (u'CTRL_expressions_mouthLowerLipDepressR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthCornerPullL', (u'CTRL_expressions_mouthCornerPullL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthCornerPullR', (u'CTRL_expressions_mouthCornerPullR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthStretchL', (u'CTRL_expressions_mouthStretchL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthStretchR', (u'CTRL_expressions_mouthStretchR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthStretchLipsCloseL', (u'CTRL_expressions_mouthStretchLipsCloseL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthStretchLipsCloseR', (u'CTRL_expressions_mouthStretchLipsCloseR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthDimpleL', (u'CTRL_expressions_mouthDimpleL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthDimpleR', (u'CTRL_expressions_mouthDimpleR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthCornerDepressL', (u'CTRL_expressions_mouthCornerDepressL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthCornerDepressR', (u'CTRL_expressions_mouthCornerDepressR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthPressUL', (u'CTRL_expressions_mouthPressUL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthPressUR', (u'CTRL_expressions_mouthPressUR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthPressDL', (u'CTRL_expressions_mouthPressDL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthPressDR', (u'CTRL_expressions_mouthPressDR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsPurseUL', (u'CTRL_expressions_mouthLipsPurseUL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsPurseUR', (u'CTRL_expressions_mouthLipsPurseUR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsPurseDL', (u'CTRL_expressions_mouthLipsPurseDL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsPurseDR', (u'CTRL_expressions_mouthLipsPurseDR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsTowardsUL', (u'CTRL_expressions_mouthLipsTowardsUL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsTowardsUR', (u'CTRL_expressions_mouthLipsTowardsUR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsTowardsDL', (u'CTRL_expressions_mouthLipsTowardsDL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsTowardsDR', (u'CTRL_expressions_mouthLipsTowardsDR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthFunnelUL', (u'CTRL_expressions_mouthFunnelUL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthFunnelUR', (u'CTRL_expressions_mouthFunnelUR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthFunnelDL', (u'CTRL_expressions_mouthFunnelDL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthFunnelDR', (u'CTRL_expressions_mouthFunnelDR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsTogetherUL', (u'CTRL_expressions_mouthLipsTogetherUL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsTogetherUR', (u'CTRL_expressions_mouthLipsTogetherUR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsTogetherDL', (u'CTRL_expressions_mouthLipsTogetherDL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsTogetherDR', (u'CTRL_expressions_mouthLipsTogetherDR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthUpperLipBiteL', (u'CTRL_expressions_mouthUpperLipBiteL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthUpperLipBiteR', (u'CTRL_expressions_mouthUpperLipBiteR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLowerLipBiteL', (u'CTRL_expressions_mouthLowerLipBiteL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLowerLipBiteR', (u'CTRL_expressions_mouthLowerLipBiteR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsTightenUL', (u'CTRL_expressions_mouthLipsTightenUL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsTightenUR', (u'CTRL_expressions_mouthLipsTightenUR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsTightenDL', (u'CTRL_expressions_mouthLipsTightenDL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsTightenDR', (u'CTRL_expressions_mouthLipsTightenDR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsPressL', (u'CTRL_expressions_mouthLipsPressL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsPressR', (u'CTRL_expressions_mouthLipsPressR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthSharpCornerPullL', (u'CTRL_expressions_mouthSharpCornerPullL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthSharpCornerPullR', (u'CTRL_expressions_mouthSharpCornerPullR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthStickyUC', (u'CTRL_expressions_mouthStickyUC', 0.0, 1.0)),
 (u'CTRL_expressions.mouthStickyUINL', (u'CTRL_expressions_mouthStickyUINL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthStickyUINR', (u'CTRL_expressions_mouthStickyUINR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthStickyUOUTL', (u'CTRL_expressions_mouthStickyUOUTL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthStickyUOUTR', (u'CTRL_expressions_mouthStickyUOUTR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthStickyDC', (u'CTRL_expressions_mouthStickyDC', 0.0, 1.0)),
 (u'CTRL_expressions.mouthStickyDINL', (u'CTRL_expressions_mouthStickyDINL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthStickyDINR', (u'CTRL_expressions_mouthStickyDINR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthStickyDOUTL', (u'CTRL_expressions_mouthStickyDOUTL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthStickyDOUTR', (u'CTRL_expressions_mouthStickyDOUTR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsStickyLPh1', (u'CTRL_expressions_mouthLipsStickyLPh1', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsStickyLPh2', (u'CTRL_expressions_mouthLipsStickyLPh2', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsStickyLPh3', (u'CTRL_expressions_mouthLipsStickyLPh3', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsStickyRPh1', (u'CTRL_expressions_mouthLipsStickyRPh1', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsStickyRPh2', (u'CTRL_expressions_mouthLipsStickyRPh2', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsStickyRPh3', (u'CTRL_expressions_mouthLipsStickyRPh3', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsPushUL', (u'CTRL_expressions_mouthLipsPushUL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsPushUR', (u'CTRL_expressions_mouthLipsPushUR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsPushDL', (u'CTRL_expressions_mouthLipsPushDL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsPushDR', (u'CTRL_expressions_mouthLipsPushDR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsPullUL', (u'CTRL_expressions_mouthLipsPullUL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsPullUR', (u'CTRL_expressions_mouthLipsPullUR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsPullDL', (u'CTRL_expressions_mouthLipsPullDL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsPullDR', (u'CTRL_expressions_mouthLipsPullDR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsThinUL', (u'CTRL_expressions_mouthLipsThinUL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsThinUR', (u'CTRL_expressions_mouthLipsThinUR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsThinDL', (u'CTRL_expressions_mouthLipsThinDL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsThinDR', (u'CTRL_expressions_mouthLipsThinDR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsThickUL', (u'CTRL_expressions_mouthLipsThickUL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsThickUR', (u'CTRL_expressions_mouthLipsThickUR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsThickDL', (u'CTRL_expressions_mouthLipsThickDL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLipsThickDR', (u'CTRL_expressions_mouthLipsThickDR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthCornerSharpenUL', (u'CTRL_expressions_mouthCornerSharpenUL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthCornerSharpenUR', (u'CTRL_expressions_mouthCornerSharpenUR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthCornerSharpenDL', (u'CTRL_expressions_mouthCornerSharpenDL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthCornerSharpenDR', (u'CTRL_expressions_mouthCornerSharpenDR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthCornerRounderUL', (u'CTRL_expressions_mouthCornerRounderUL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthCornerRounderUR', (u'CTRL_expressions_mouthCornerRounderUR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthCornerRounderDL', (u'CTRL_expressions_mouthCornerRounderDL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthCornerRounderDR', (u'CTRL_expressions_mouthCornerRounderDR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthUpperLipTowardsTeethL', (u'CTRL_expressions_mouthUpperLipTowardsTeethL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthUpperLipTowardsTeethR', (u'CTRL_expressions_mouthUpperLipTowardsTeethR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLowerLipTowardsTeethL', (u'CTRL_expressions_mouthLowerLipTowardsTeethL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLowerLipTowardsTeethR', (u'CTRL_expressions_mouthLowerLipTowardsTeethR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthUpperLipShiftLeft', (u'CTRL_expressions_mouthUpperLipShiftLeft', 0.0, 1.0)),
 (u'CTRL_expressions.mouthUpperLipShiftRight', (u'CTRL_expressions_mouthUpperLipShiftRight', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLowerLipShiftLeft', (u'CTRL_expressions_mouthLowerLipShiftLeft', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLowerLipShiftRight', (u'CTRL_expressions_mouthLowerLipShiftRight', 0.0, 1.0)),
 (u'CTRL_expressions.mouthUpperLipRollInL', (u'CTRL_expressions_mouthUpperLipRollInL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthUpperLipRollInR', (u'CTRL_expressions_mouthUpperLipRollInR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthUpperLipRollOutL', (u'CTRL_expressions_mouthUpperLipRollOutL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthUpperLipRollOutR', (u'CTRL_expressions_mouthUpperLipRollOutR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLowerLipRollInL', (u'CTRL_expressions_mouthLowerLipRollInL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLowerLipRollInR', (u'CTRL_expressions_mouthLowerLipRollInR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLowerLipRollOutL', (u'CTRL_expressions_mouthLowerLipRollOutL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthLowerLipRollOutR', (u'CTRL_expressions_mouthLowerLipRollOutR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthCornerUpL', (u'CTRL_expressions_mouthCornerUpL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthCornerUpR', (u'CTRL_expressions_mouthCornerUpR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthCornerDownL', (u'CTRL_expressions_mouthCornerDownL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthCornerDownR', (u'CTRL_expressions_mouthCornerDownR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthCornerWideL', (u'CTRL_expressions_mouthCornerWideL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthCornerWideR', (u'CTRL_expressions_mouthCornerWideR', 0.0, 1.0)),
 (u'CTRL_expressions.mouthCornerNarrowL', (u'CTRL_expressions_mouthCornerNarrowL', 0.0, 1.0)),
 (u'CTRL_expressions.mouthCornerNarrowR', (u'CTRL_expressions_mouthCornerNarrowR', 0.0, 1.0)),
 (u'CTRL_expressions.tongueUp', (u'CTRL_expressions_tongueUp', 0.0, 1.0)),
 (u'CTRL_expressions.tongueDown', (u'CTRL_expressions_tongueDown', 0.0, 1.0)),
 (u'CTRL_expressions.tongueLeft', (u'CTRL_expressions_tongueLeft', 0.0, 1.0)),
 (u'CTRL_expressions.tongueRight', (u'CTRL_expressions_tongueRight', 0.0, 1.0)),
 (u'CTRL_expressions.tongueOut', (u'CTRL_expressions_tongueOut', 0.0, 1.0)),
 (u'CTRL_expressions.tongueIn', (u'CTRL_expressions_tongueIn', 0.0, 1.0)),
 (u'CTRL_expressions.tongueRollUp', (u'CTRL_expressions_tongueRollUp', 0.0, 1.0)),
 (u'CTRL_expressions.tongueRollDown', (u'CTRL_expressions_tongueRollDown', 0.0, 1.0)),
 (u'CTRL_expressions.tongueRollLeft', (u'CTRL_expressions_tongueRollLeft', 0.0, 1.0)),
 (u'CTRL_expressions.tongueRollRight', (u'CTRL_expressions_tongueRollRight', 0.0, 1.0)),
 (u'CTRL_expressions.tongueTipUp', (u'CTRL_expressions_tongueTipUp', 0.0, 1.0)),
 (u'CTRL_expressions.tongueTipDown', (u'CTRL_expressions_tongueTipDown', 0.0, 1.0)),
 (u'CTRL_expressions.tongueTipLeft', (u'CTRL_expressions_tongueTipLeft', 0.0, 1.0)),
 (u'CTRL_expressions.tongueTipRight', (u'CTRL_expressions_tongueTipRight', 0.0, 1.0)),
 (u'CTRL_expressions.tongueWide', (u'CTRL_expressions_tongueWide', 0.0, 1.0)),
 (u'CTRL_expressions.tongueNarrow', (u'CTRL_expressions_tongueNarrow', 0.0, 1.0)),
 (u'CTRL_expressions.tonguePress', (u'CTRL_expressions_tonguePress', 0.0, 1.0)),
 (u'CTRL_expressions.jawOpen', (u'CTRL_expressions_jawOpen', 0.0, 1.0)),
 (u'CTRL_expressions.jawLeft', (u'CTRL_expressions_jawLeft', 0.0, 1.0)),
 (u'CTRL_expressions.jawRight', (u'CTRL_expressions_jawRight', 0.0, 1.0)),
 (u'CTRL_expressions.jawFwd', (u'CTRL_expressions_jawFwd', 0.0, 1.0)),
 (u'CTRL_expressions.jawBack', (u'CTRL_expressions_jawBack', 0.0, 1.0)),
 (u'CTRL_expressions.jawClenchL', (u'CTRL_expressions_jawClenchL', 0.0, 1.0)),
 (u'CTRL_expressions.jawClenchR', (u'CTRL_expressions_jawClenchR', 0.0, 1.0)),
 (u'CTRL_expressions.jawChinRaiseDL', (u'CTRL_expressions_jawChinRaiseDL', 0.0, 1.0)),
 (u'CTRL_expressions.jawChinRaiseDR', (u'CTRL_expressions_jawChinRaiseDR', 0.0, 1.0)),
 (u'CTRL_expressions.jawChinRaiseUL', (u'CTRL_expressions_jawChinRaiseUL', 0.0, 1.0)),
 (u'CTRL_expressions.jawChinRaiseUR', (u'CTRL_expressions_jawChinRaiseUR', 0.0, 1.0)),
 (u'CTRL_expressions.jawChinCompressL', (u'CTRL_expressions_jawChinCompressL', 0.0, 1.0)),
 (u'CTRL_expressions.jawChinCompressR', (u'CTRL_expressions_jawChinCompressR', 0.0, 1.0)),
 (u'CTRL_expressions.jawOpenExtreme', (u'CTRL_expressions_jawOpenExtreme', 0.0, 1.0)),
 (u'CTRL_expressions.neckStretchL', (u'CTRL_expressions_neckStretchL', 0.0, 1.0)),
 (u'CTRL_expressions.neckStretchR', (u'CTRL_expressions_neckStretchR', 0.0, 1.0)),
 (u'CTRL_expressions.neckSwallowPh1', (u'CTRL_expressions_neckSwallowPh1', 0.0, 1.0)),
 (u'CTRL_expressions.neckSwallowPh2', (u'CTRL_expressions_neckSwallowPh2', 0.0, 1.0)),
 (u'CTRL_expressions.neckSwallowPh3', (u'CTRL_expressions_neckSwallowPh3', 0.0, 1.0)),
 (u'CTRL_expressions.neckSwallowPh4', (u'CTRL_expressions_neckSwallowPh4', 0.0, 1.0)),
 (u'CTRL_expressions.neckMastoidContractL', (u'CTRL_expressions_neckMastoidContractL', 0.0, 1.0)),
 (u'CTRL_expressions.neckMastoidContractR', (u'CTRL_expressions_neckMastoidContractR', 0.0, 1.0)),
 (u'CTRL_expressions.neckThroatDown', (u'CTRL_expressions_neckThroatDown', 0.0, 1.0)),
 (u'CTRL_expressions.neckThroatUp', (u'CTRL_expressions_neckThroatUp', 0.0, 1.0)),
 (u'CTRL_expressions.neckDigastricDown', (u'CTRL_expressions_neckDigastricDown', 0.0, 1.0)),
 (u'CTRL_expressions.neckDigastricUp', (u'CTRL_expressions_neckDigastricUp', 0.0, 1.0)),
 (u'CTRL_expressions.neckThroatExhale', (u'CTRL_expressions_neckThroatExhale', 0.0, 1.0)),
 (u'CTRL_expressions.neckThroatInhale', (u'CTRL_expressions_neckThroatInhale', 0.0, 1.0)),
 (u'CTRL_expressions.teethUpU', (u'CTRL_expressions_teethUpU', 0.0, 1.0)),
 (u'CTRL_expressions.teethUpD', (u'CTRL_expressions_teethUpD', 0.0, 1.0)),
 (u'CTRL_expressions.teethDownU', (u'CTRL_expressions_teethDownU', 0.0, 1.0)),
 (u'CTRL_expressions.teethDownD', (u'CTRL_expressions_teethDownD', 0.0, 1.0)),
 (u'CTRL_expressions.teethLeftU', (u'CTRL_expressions_teethLeftU', 0.0, 1.0)),
 (u'CTRL_expressions.teethLeftD', (u'CTRL_expressions_teethLeftD', 0.0, 1.0)),
 (u'CTRL_expressions.teethRightU', (u'CTRL_expressions_teethRightU', 0.0, 1.0)),
 (u'CTRL_expressions.teethRightD', (u'CTRL_expressions_teethRightD', 0.0, 1.0)),
 (u'CTRL_expressions.teethFwdU', (u'CTRL_expressions_teethFwdU', 0.0, 1.0)),
 (u'CTRL_expressions.teethFwdD', (u'CTRL_expressions_teethFwdD', 0.0, 1.0)),
 (u'CTRL_expressions.teethBackU', (u'CTRL_expressions_teethBackU', 0.0, 1.0)),
 (u'CTRL_expressions.teethBackD', (u'CTRL_expressions_teethBackD', 0.0, 1.0)),
 (u'CTRL_expressions.headTurnUpCor', (u'CTRL_expressions_headTurnUpCor', 0.0, 1.0)),
 (u'CTRL_expressions.headTurnDownCor', (u'CTRL_expressions_headTurnDownCor', 0.0, 1.0)),
 (u'CTRL_expressions.headTurnLeftCor', (u'CTRL_expressions_headTurnLeftCor', 0.0, 1.0)),
 (u'CTRL_expressions.headTurnRightCor', (u'CTRL_expressions_headTurnRightCor', 0.0, 1.0)),
 (u'CTRL_expressions.headTiltLeftCor', (u'CTRL_expressions_headTiltLeftCor', 0.0, 1.0)),
 (u'CTRL_expressions.headTiltRightCor', (u'CTRL_expressions_headTiltRightCor', 0.0, 1.0)),
 (u'CTRL_expressions.headFwdCor', (u'CTRL_expressions_headFwdCor', 0.0, 1.0)),
 (u'CTRL_expressions.headBackCor', (u'CTRL_expressions_headBackCor', 0.0, 1.0)),
 (u'CTRL_expressions.headSideLeftCor', (u'CTRL_expressions_headSideLeftCor', 0.0, 1.0)),
 (u'CTRL_expressions.headSideRightCor', (u'CTRL_expressions_headSideRightCor', 0.0, 1.0)),
 (u'CTRL_expressions.skullUnified', (u'CTRL_expressions_skullUnified', 0.0, 1.0)),
 (u'CTRL_expressions.bodyNeckFemaleAverageCor', (u'CTRL_expressions_bodyNeckFemaleAverageCor', 0.0, 1.0)),
 (u'CTRL_expressions.bodyNeckMaleMuscularCor', (u'CTRL_expressions_bodyNeckMaleMuscularCor', 0.0, 1.0)),
 (u'CTRL_rigLogic.OffOn', (u'CTRL_rigLogic_OffOn', 0.0, 1.0))])

WM_CONTROL_NAME = "FRM_WMmultipliers"

WM_ATTRIBUTES = ["head_wm2_normal_head_wm2_browsDown_L",
 "head_cm2_color_head_wm2_browsDown_L",
 "head_wm2_normal_head_wm2_browsDown_R",
 "head_cm2_color_head_wm2_browsDown_R",
 "head_wm2_normal_head_wm2_browsLateral_L",
 "head_cm2_color_head_wm2_browsLateral_L",
 "head_wm2_normal_head_wm2_browsLateral_R",
 "head_cm2_color_head_wm2_browsLateral_R",
 "head_wm1_normal_head_wm1_browsRaiseInner_",
 "head_cm1_color_head_wm1_browsRaiseInner_L",
 "head_wm1_normal_head_wm1_browsRaiseInner_",
 "head_cm1_color_head_wm1_browsRaiseInner_",
 "head_cm1_color_head_wm1_browsRaiseOuter_L",
 "head_wm1_normal_head_wm1_browsRaiseOuter_L",
 "head_wm1_normal_head_wm1_browsRaiseOuter_R",
 "head_cm1_color_head_wm1_browsRaiseOuter_",
 "head_cm1_color_head_wm1_blink_L",
 "head_wm1_normal_head_wm1_blink_L",
 "head_cm1_color_head_wm1_squintInner_",
 "head_wm1_normal_head_wm1_squintInner_L",
 "head_cm1_color_head_wm1_blink_R",
 "head_wm1_normal_head_wm1_squintInner_R",
 "head_cm1_color_head_wm1_squintInner_R",
 "head_wm1_normal_head_wm1_blink_R",
 "head_cm3_color_head_wm3_cheekRaiseUpper_",
 "head_cm3_color_head_wm3_cheekRaiseInner_L",
 "head_wm3_normal_head_wm3_cheekRaiseUpper_L",
 "head_wm3_normal_head_wm3_cheekRaiseOuter_L",
 "head_cm3_color_head_wm3_cheekRaiseOuter_",
 "head_wm3_normal_head_wm3_cheekRaiseInner_L",
 "head_wm3_normal_head_wm3_cheekRaiseUpper_",
 "head_cm3_color_head_wm3_cheekRaiseInner_",
 "head_cm3_color_head_wm3_cheekRaiseUpper_R",
 "head_wm3_normal_head_wm3_cheekRaiseInner_",
 "head_cm3_color_head_wm3_cheekRaiseOuter_",
 "head_wm3_normal_head_wm3_cheekRaiseOuter_",
 "head_cm2_color_head_wm2_noseWrinkler_L",
 "head_wm2_normal_head_wm2_noseWrinkler_L",
 "head_cm2_color_head_wm2_noseWrinkler_R",
 "head_wm2_normal_head_wm2_noseWrinkler_",
 "head_cm1_color_head_wm13_lips_UR",
 "head_wm1_normal_head_wm13_lips_UR",
 "head_cm1_color_head_wm13_lips_DR",
 "head_cm1_color_head_wm13_lips_D",
 "head_wm1_normal_head_wm13_lips_UL",
 "head_cm1_color_head_wm13_lips_UL",
 "head_wm1_normal_head_wm13_lips_DR",
 "head_wm1_normal_head_wm13_lips_DL",
 "head_wm3_normal_head_wm3_smile_",
 "head_cm3_color_head_wm3_smile_L",
 "head_cm3_color_head_wm3_smile_",
 "head_wm3_normal_head_wm3_smile_",
 "head_wm3_normal_head_wm13_lips_U",
 "head_cm3_color_head_wm13_lips_UL",
 "head_wm3_normal_head_wm13_lips_DL",
 "head_cm3_color_head_wm13_lips_DL",
 "head_wm3_normal_head_wm13_lips_D",
 "head_cm3_color_head_wm13_lips_UR",
 "head_wm3_normal_head_wm13_lips_UR",
 "head_cm3_color_head_wm13_lips_D",
 "head_cm2_color_head_wm2_mouthStretch_L",
 "head_wm2_normal_head_wm2_mouthStretch_L",
 "head_wm2_normal_head_wm2_mouthStretch_",
 "head_cm2_color_head_wm2_mouthStretch_",
 "head_wm1_normal_head_wm1_purse_U",
 "head_cm1_color_head_wm1_purse_U",
 "head_cm1_color_head_wm1_purse_UR",
 "head_wm1_normal_head_wm1_purse_UR",
 "head_cm1_color_head_wm1_purse_DL",
 "head_wm1_normal_head_wm1_purse_DL",
 "head_cm1_color_head_wm1_purse_DR",
 "head_wm1_normal_head_wm1_purse_D",
 "head_wm1_normal_head_wm1_chinRaise_",
 "head_cm1_color_head_wm1_chinRaise_",
 "head_cm1_color_head_wm1_chinRaise_R",
 "head_wm1_normal_head_wm1_chinRaise_R",
 "head_cm1_color_head_wm1_jawOpen",
 "head_wm1_normal_head_wm1_jawOpen",
 "head_cm2_color_head_wm2_neckStretch_L",
 "head_wm2_normal_head_wm2_neckStretch_L",
 "head_wm2_normal_head_wm2_neckStretch_R",
 "head_cm2_color_head_wm2_neckStretch_R"]

COMMON_MAP_INFOS = [("dx11_diffuseIrradiance", 1),
("dx11_jitter", 1),
("dx11_skinLUT", 1),
("dx11_specularIrradiance", 1)]

COMMON_MAP_INFOS_BODY = [("dx11_diffuseIrradiance_b", 1),
("dx11_jitter_b", 1),
("dx11_skinLUT_b", 1),
("dx11_specularIrradiance_b", 1)]

MAP_INFOS = [
("head_color", 1),
("head_cm1_color", 0),
("head_cm2_color", 0),
("head_cm3_color", 0),
("head_normal", 1),
("head_wm1_normal", 0),
("head_wm2_normal", 0),
("head_wm3_normal", 0),
("head_specular", 1),
("head_specular_16Bits", 1),
("head_occlusion", 1),
("head_occlusion_16Bits", 1),
("head_cavity", 1),
("head_cavity_16Bits", 1),
("head_transmission", 1),
("head_transmission_16Bits", 1),
("head_curvature", 1),
("head_curvature_16Bits", 1),
("head_position", 1),
("head_position_16Bits", 1),
("head_worldspace", 1),
("head_worldspace_16Bits", 1),
("head_bentNormal", 1),
("head_bentNormal_16Bits", 1),
("teeth_color", 1),
("teeth_normal", 1),
("eyes_color", 1),
("eyeLeft_color", 1),
("eyeRight_color", 1),
("eyeLeft_normal", 1),
("eyeRight_normal", 1),
("eyes_color_16Bits", 1),
("eyes_normal", 1),
("eyes_normal_16Bits", 1),
("eyelashes_color", 1)]

BODY_MAP_INFOS = [("body_color", 1), ("body_normal", 1), ("body_cavity", 1)]

MASKS = [u'head_wm1_blink_L',
 u'head_wm1_blink_R',
 u'head_wm1_browsRaiseInner_L',
 u'head_wm1_browsRaiseInner_R',
 u'head_wm1_browsRaiseOuter_L',
 u'head_wm1_browsRaiseOuter_R',
 u'head_wm1_chinRaise_L',
 u'head_wm1_chinRaise_R',
 u'head_wm1_jawOpen',
 u'head_wm1_purse_DL',
 u'head_wm1_purse_DR',
 u'head_wm1_purse_UL',
 u'head_wm1_purse_UR',
 u'head_wm1_squintInner_L',
 u'head_wm1_squintInner_R',
 u'head_wm2_browsDown_L',
 u'head_wm2_browsDown_R',
 u'head_wm2_browsLateral_L',
 u'head_wm2_browsLateral_R',
 u'head_wm2_mouthStretch_L',
 u'head_wm2_mouthStretch_R',
 u'head_wm2_neckStretch_L',
 u'head_wm2_neckStretch_R',
 u'head_wm2_noseWrinkler_L',
 u'head_wm2_noseWrinkler_R',
 u'head_wm3_cheekRaiseInner_L',
 u'head_wm3_cheekRaiseInner_R',
 u'head_wm3_cheekRaiseOuter_L',
 u'head_wm3_cheekRaiseOuter_R',
 u'head_wm3_cheekRaiseUpper_L',
 u'head_wm3_cheekRaiseUpper_R',
 u'head_wm3_smile_L',
 u'head_wm3_smile_R',
 u'head_wm13_lips_DL',
 u'head_wm13_lips_DR',
 u'head_wm13_lips_UL',
 u'head_wm13_lips_UR']

MESH_SHADER_MAPPING = {'head_lod': u'head_shader',
 'teeth_lod': u'teeth_shader',
 'saliva_lod': u'saliva_shader',
 'eyeLeft_lod': u'eyeLeft_shader',
 'eyeRight_lod': u'eyeRight_shader',
 'eyeshell_lod': u'eyeshell_shader',
 'eyelashes_lod': u'eyelashes_shader',
 'eyelashesShadow_lod': u'eyelashesShadow_shader',
 'eyeEdge_lod': u'eyeEdge_shader',
 'cartilage_lod': 'eyeEdge_shader'
}

SHADERS = ['head_shader', 'teeth_shader', 'eyeLeft_shader', 'eyeRight_shader']
BODY_SHADERS = ['body_shader']

FLIP_FLOP_SHADERS = [("flipflops_baseColor", 1), ("flipflops_normalMap", 1)]

SHADER_ATTRIBUTES_MAPPING = {"FRM_WMmultipliers.head_cm2_color_head_wm2_browsDown_L": "shader_head_shader.maskWeight_00",
 "FRM_WMmultipliers.head_wm2_normal_head_wm2_browsDown_L": "shader_head_shader.maskWeight_01",
 "FRM_WMmultipliers.head_cm2_color_head_wm2_browsDown_R": "shader_head_shader.maskWeight_02",
 "FRM_WMmultipliers.head_wm2_normal_head_wm2_browsDown_R": "shader_head_shader.maskWeight_03",
 "FRM_WMmultipliers.head_cm2_color_head_wm2_browsLateral_L": "shader_head_shader.maskWeight_04",
 "FRM_WMmultipliers.head_wm2_normal_head_wm2_browsLateral_L": "shader_head_shader.maskWeight_05",
 "FRM_WMmultipliers.head_cm2_color_head_wm2_browsLateral_R": "shader_head_shader.maskWeight_06",
 "FRM_WMmultipliers.head_wm2_normal_head_wm2_browsLateral_R": "shader_head_shader.maskWeight_07",
 "FRM_WMmultipliers.head_cm1_color_head_wm1_browsRaiseInner_L": "shader_head_shader.maskWeight_08",
 "FRM_WMmultipliers.head_wm1_normal_head_wm1_browsRaiseInner_L": "shader_head_shader.maskWeight_09",
 "FRM_WMmultipliers.head_cm1_color_head_wm1_browsRaiseInner_R": "shader_head_shader.maskWeight_10",
 "FRM_WMmultipliers.head_wm1_normal_head_wm1_browsRaiseInner_R": "shader_head_shader.maskWeight_11",
 "FRM_WMmultipliers.head_cm1_color_head_wm1_browsRaiseOuter_L": "shader_head_shader.maskWeight_12",
 "FRM_WMmultipliers.head_wm1_normal_head_wm1_browsRaiseOuter_L": "shader_head_shader.maskWeight_13",
 "FRM_WMmultipliers.head_cm1_color_head_wm1_browsRaiseOuter_R": "shader_head_shader.maskWeight_14",
 "FRM_WMmultipliers.head_wm1_normal_head_wm1_browsRaiseOuter_R": "shader_head_shader.maskWeight_15",
 "FRM_WMmultipliers.head_cm1_color_head_wm1_blink_L": "shader_head_shader.maskWeight_16",
 "FRM_WMmultipliers.head_cm1_color_head_wm1_squintInner_L": "shader_head_shader.maskWeight_17",
 "FRM_WMmultipliers.head_wm1_normal_head_wm1_blink_L": "shader_head_shader.maskWeight_18",
 "FRM_WMmultipliers.head_wm1_normal_head_wm1_squintInner_L": "shader_head_shader.maskWeight_19",
 "FRM_WMmultipliers.head_cm1_color_head_wm1_blink_R": "shader_head_shader.maskWeight_20",
 "FRM_WMmultipliers.head_cm1_color_head_wm1_squintInner_R": "shader_head_shader.maskWeight_21",
 "FRM_WMmultipliers.head_wm1_normal_head_wm1_blink_R": "shader_head_shader.maskWeight_22",
 "FRM_WMmultipliers.head_wm1_normal_head_wm1_squintInner_R": "shader_head_shader.maskWeight_23",
 "FRM_WMmultipliers.head_cm3_color_head_wm3_cheekRaiseInner_L": "shader_head_shader.maskWeight_24",
 "FRM_WMmultipliers.head_cm3_color_head_wm3_cheekRaiseOuter_L": "shader_head_shader.maskWeight_25",
 "FRM_WMmultipliers.head_cm3_color_head_wm3_cheekRaiseUpper_L": "shader_head_shader.maskWeight_26",
 "FRM_WMmultipliers.head_wm3_normal_head_wm3_cheekRaiseInner_L": "shader_head_shader.maskWeight_27",
 "FRM_WMmultipliers.head_wm3_normal_head_wm3_cheekRaiseOuter_L": "shader_head_shader.maskWeight_28",
 "FRM_WMmultipliers.head_wm3_normal_head_wm3_cheekRaiseUpper_L": "shader_head_shader.maskWeight_29",
 "FRM_WMmultipliers.head_cm3_color_head_wm3_cheekRaiseInner_R": "shader_head_shader.maskWeight_30",
 "FRM_WMmultipliers.head_cm3_color_head_wm3_cheekRaiseOuter_R": "shader_head_shader.maskWeight_31",
 "FRM_WMmultipliers.head_cm3_color_head_wm3_cheekRaiseUpper_R": "shader_head_shader.maskWeight_32",
 "FRM_WMmultipliers.head_wm3_normal_head_wm3_cheekRaiseInner_R": "shader_head_shader.maskWeight_33",
 "FRM_WMmultipliers.head_wm3_normal_head_wm3_cheekRaiseOuter_R": "shader_head_shader.maskWeight_34",
 "FRM_WMmultipliers.head_wm3_normal_head_wm3_cheekRaiseUpper_R": "shader_head_shader.maskWeight_35",
 "FRM_WMmultipliers.head_cm2_color_head_wm2_noseWrinkler_L": "shader_head_shader.maskWeight_36",
 "FRM_WMmultipliers.head_wm2_normal_head_wm2_noseWrinkler_L": "shader_head_shader.maskWeight_37",
 "FRM_WMmultipliers.head_cm2_color_head_wm2_noseWrinkler_R": "shader_head_shader.maskWeight_38",
 "FRM_WMmultipliers.head_wm2_normal_head_wm2_noseWrinkler_R": "shader_head_shader.maskWeight_39",
 "FRM_WMmultipliers.head_cm3_color_head_wm3_smile_L": "shader_head_shader.maskWeight_40",
 "FRM_WMmultipliers.head_wm3_normal_head_wm3_smile_L": "shader_head_shader.maskWeight_41",
 "FRM_WMmultipliers.head_cm1_color_head_wm13_lips_UL": "shader_head_shader.maskWeight_42",
 "FRM_WMmultipliers.head_cm1_color_head_wm13_lips_UR": "shader_head_shader.maskWeight_43",
 "FRM_WMmultipliers.head_cm1_color_head_wm13_lips_DL": "shader_head_shader.maskWeight_44",
 "FRM_WMmultipliers.head_cm1_color_head_wm13_lips_DR": "shader_head_shader.maskWeight_45",
 "FRM_WMmultipliers.head_wm1_normal_head_wm13_lips_UL": "shader_head_shader.maskWeight_46",
 "FRM_WMmultipliers.head_wm1_normal_head_wm13_lips_UR": "shader_head_shader.maskWeight_47",
 "FRM_WMmultipliers.head_wm1_normal_head_wm13_lips_DL": "shader_head_shader.maskWeight_48",
 "FRM_WMmultipliers.head_wm1_normal_head_wm13_lips_DR": "shader_head_shader.maskWeight_49",
 "FRM_WMmultipliers.head_cm3_color_head_wm3_smile_R": "shader_head_shader.maskWeight_50",
 "FRM_WMmultipliers.head_wm3_normal_head_wm3_smile_R": "shader_head_shader.maskWeight_51",
 "FRM_WMmultipliers.head_cm3_color_head_wm13_lips_UL": "shader_head_shader.maskWeight_52",
 "FRM_WMmultipliers.head_cm3_color_head_wm13_lips_DL": "shader_head_shader.maskWeight_53",
 "FRM_WMmultipliers.head_wm3_normal_head_wm13_lips_UL": "shader_head_shader.maskWeight_54",
 "FRM_WMmultipliers.head_wm3_normal_head_wm13_lips_DL": "shader_head_shader.maskWeight_55",
 "FRM_WMmultipliers.head_cm3_color_head_wm13_lips_UR": "shader_head_shader.maskWeight_56",
 "FRM_WMmultipliers.head_cm3_color_head_wm13_lips_DR": "shader_head_shader.maskWeight_57",
 "FRM_WMmultipliers.head_wm3_normal_head_wm13_lips_UR": "shader_head_shader.maskWeight_58",
 "FRM_WMmultipliers.head_wm3_normal_head_wm13_lips_DR": "shader_head_shader.maskWeight_59",
 "FRM_WMmultipliers.head_cm2_color_head_wm2_mouthStretch_L": "shader_head_shader.maskWeight_60",
 "FRM_WMmultipliers.head_wm2_normal_head_wm2_mouthStretch_L": "shader_head_shader.maskWeight_61",
 "FRM_WMmultipliers.head_cm2_color_head_wm2_mouthStretch_R": "shader_head_shader.maskWeight_62",
 "FRM_WMmultipliers.head_wm2_normal_head_wm2_mouthStretch_R": "shader_head_shader.maskWeight_63",
 "FRM_WMmultipliers.head_cm1_color_head_wm1_purse_UL": "shader_head_shader.maskWeight_64",
 "FRM_WMmultipliers.head_wm1_normal_head_wm1_purse_UL": "shader_head_shader.maskWeight_65",
 "FRM_WMmultipliers.head_cm1_color_head_wm1_purse_UR": "shader_head_shader.maskWeight_66",
 "FRM_WMmultipliers.head_wm1_normal_head_wm1_purse_UR": "shader_head_shader.maskWeight_67",
 "FRM_WMmultipliers.head_cm1_color_head_wm1_purse_DL": "shader_head_shader.maskWeight_68",
 "FRM_WMmultipliers.head_wm1_normal_head_wm1_purse_DL": "shader_head_shader.maskWeight_69",
 "FRM_WMmultipliers.head_cm1_color_head_wm1_purse_DR": "shader_head_shader.maskWeight_70",
 "FRM_WMmultipliers.head_wm1_normal_head_wm1_purse_DR": "shader_head_shader.maskWeight_71",
 "FRM_WMmultipliers.head_cm1_color_head_wm1_chinRaise_L": "shader_head_shader.maskWeight_72",
 "FRM_WMmultipliers.head_wm1_normal_head_wm1_chinRaise_L": "shader_head_shader.maskWeight_73",
 "FRM_WMmultipliers.head_cm1_color_head_wm1_chinRaise_R": "shader_head_shader.maskWeight_74",
 "FRM_WMmultipliers.head_wm1_normal_head_wm1_chinRaise_R": "shader_head_shader.maskWeight_75",
 "FRM_WMmultipliers.head_cm1_color_head_wm1_jawOpen": "shader_head_shader.maskWeight_76",
 "FRM_WMmultipliers.head_wm1_normal_head_wm1_jawOpen": "shader_head_shader.maskWeight_77",
 "FRM_WMmultipliers.head_cm2_color_head_wm2_neckStretch_L": "shader_head_shader.maskWeight_78",
 "FRM_WMmultipliers.head_wm2_normal_head_wm2_neckStretch_L": "shader_head_shader.maskWeight_79",
 "FRM_WMmultipliers.head_cm2_color_head_wm2_neckStretch_R": "shader_head_shader.maskWeight_80",
 "FRM_WMmultipliers.head_wm2_normal_head_wm2_neckStretch_R": "shader_head_shader.maskWeight_81"}

MARKER_MESH_NAME = "head_lod0_mesh"
MARKER_VTX_ID = [8, 50, 596, 820, 863, 948, 979, 1313, 2046, 2047, 2049, 2268, 2298, 2471, 2879, 2910, 2935, 2949, 2959, 2982, 2988, 3033, 3079, 3121, 3667, 3891, 3934, 4019, 4050, 4384, 5117, 5118, 5120, 5339, 5369, 5542, 6002, 6018, 6135, 6405, 7518, 7547, 8020, 8143, 9383, 10251, 11424, 11754, 12074, 12352, 12691, 13500, 13529, 14000, 14121, 15368, 15834, 16252, 16958, 17088, 17113, 17468, 17810, 19617, 19903, 20118, 22630, 22916, 23131]
