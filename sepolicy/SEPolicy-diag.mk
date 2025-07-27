ifneq (,$(filter user, $(TARGET_BUILD_VARIANT)))
BOARD_VENDOR_SEPOLICY_DIRS += $(DEVICE_PATH)/sepolicy/diag
endif
