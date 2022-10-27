#!/usr/intel/bin/tcsh
source /p/hdk/rtl/hdk.rc -cfg shdk74
setenv GECCO_POOL fm_zse
setenv MODEL_ROOT /nfs/site/disks/ive_gnr_035/M10_LVF2/X4/gnrsp_soc-srvr7nm-22ww19a-210
setenv ENV 1
setenv NBCLASSAPPEND "SLES12"
/nfs/site/eda/group/SYSNAME/emu/intel/gecco/1.13.2/bin/emurun \
-netbatch_opts '--log-file-dir /tmp/netbatch' \
-stop_default 7200 \
-hwrs_tracker_en \
-debug \
-tlm_trace \
-tlm_dut gnrsp_soc \
-tlm_model gnrsp_lcc_1c \
-enable_4c \
-core_tracker_en \
-guop_tracker_en \
-idi_tracker_en \
-acode_tracker_en \
-jem_port_registration_by_sw_side \
-netbatch_opts '--exec-limits "7h:8h"' \
-nbqslot /prj/sv/gnr/mdiv/standard \
-cycles 3500000000 \
-bios_fetchor_en \
-test /nfs/site/disks/dcsg_0496/users/adgronqu/GNR/TEST_CONTENT/MAX/8T/BasicMem/8T-BasicMem_SEQ_1-max_base_template.32.obj \
--ver /nfs/site/disks/ive_gnr_035/M10_LVF2/X4/gnrsp_soc-srvr7nm-22ww19a-210/target/gnrsp_soc/emu/ZS4_X4_M10_rev1 \
-mail 'S E' \
-dump_fuse_memory \
-minibios_obj /nfs/site/disks/ive_gnr_035/anuragha/M10LVF2_HDM/ubios/metro.32.1/ubios/ubios_annotated_rnr.obj \
-fwc GNR_ltssm_flits,soc_gnrio_north_ltssm_state,RAS_FWC_signals  \
-enable_cxl_xtor \
-enable_cxl_iow_c0 \
-enable_cxl_iow_c3 \
-enable_cxl_ioe_c6 \
-enable_cxl_ioe_c9 \
-enable_pcie_xtor \
-enable_pcie_iom_c5 \
-enable_pcie_iom_c4 \
-configdb_override /nfs/site/disks/ive_gnr_035/M10_LVF2/X4/gnrsp_soc-srvr7nm-22ww19a-210/emurun.dut_cfg \
-pythonsv.script /nfs/site/disks/ive_gnr_005/vperezba/GNR/model4/pythonSV/valras_lerr_all_iomca_print.py \
-pythonsv.base simics -pythonsv.path /nfs/site/disks/ive_pysv_daes_002/pythonsv_1p0_22ww17b \
-pythonsv.script_args ici -pythonsv.stub socket_gnrap_a0_1p0_VP_s1_ic.spkx \
-iosf_sb \
-ztdb \
-ztdbstart 1600000000 \
-ztdbstop 1600090000 \
-simics_post_setup_script /nfs/site/disks/ive_gnr_011/srivats3/RNR_new/ltssm_dump1.simics \
-simics_post_setup_script /nfs/site/disks/ive_gnr_011/srivats3/RNR_new/ltssm_dump.simics \
-simics_post_setup_script /nfs/site/disks/ive_gnr_011/srivats3/RNR_new/dl_active_dump.simics \
-simics_post_setup_script /nfs/site/disks/ive_gnr_011/srivats3/RNR_new/cxl_x4.simics \
-simics_post_setup_script /nfs/site/disks/ive_gnr_036/sravan/gnr_lvf2/linkerror/d1/signal_inject_value_GNR_c6_error_injection_print_link_error.simics
~

~                                                                                                                                                                                                               
~                                                                                              
