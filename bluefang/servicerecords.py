# -*- coding: utf-8 -*-

HID_PROFILE = """
<?xml version="1.0" encoding="UTF-8" ?>

<record>
  <attribute id="0x0001"> <!-- ServiceClassIDList -->
    <sequence>
      <uuid value="0x1124" />
    </sequence>
  </attribute>
  <attribute id="0x0004"> <!-- ProtocolDescriptorList -->
    <sequence>
      <sequence>
        <uuid value="0x0100" /> <!-- L2CAP -->
        <uint16 value="0x0011" />
      </sequence>
      <sequence>
        <uuid value="0x0011" />
      </sequence>
    </sequence>
  </attribute>
  <attribute id="0x0005"> <!-- BrowseGroupList -->
    <sequence>
      <uuid value="0x1002" />
    </sequence>
  </attribute>
  <attribute id="0x0006"> <!-- LanguageBaseAttributeIDList -->
    <sequence>
      <uint16 value="0x656e" /> <!-- en- (English) -->
      <uint16 value="0x006a" /> <!-- UTF-8 encoding -->
      <uint16 value="0x0100" /> <!-- PrimaryLanguageBaseId = 0 -->
    </sequence>
  </attribute>
  <attribute id="0x0009"> <!-- Bluetooth Profile Descriptor List -->
    <sequence>
      <sequence>
        <uuid value="0x1124" /> <!-- HID Profile -->
        <uint16 value="0x0100" /> <!-- L2CAP -->
      </sequence>
    </sequence>
  </attribute>
  <attribute id="0x000d"> <!-- AdditionalProtocolDescriptorLists -->
    <sequence>
      <sequence>
        <sequence>
          <uuid value="0x0100" /> <!-- L2CAP -->
          <uint16 value="0x0013" /> <!-- PSM for HID Interrupt -->
        </sequence>
        <sequence>
          <uuid value="0x0011" />
        </sequence>
      </sequence>
    </sequence>
  </attribute>
  <attribute id="0x0100">
    <text value="Omnihub Device" />
  </attribute>
  <attribute id="0x0101">
    <text value="Remote control proxy" />
  </attribute>
  <attribute id="0x0102">
    <text value="Raspberry Pi" />
  </attribute>
  <attribute id="0x0200"> <!-- HIDDeviceReleaseNumber (Deprecated) -->
    <uint16 value="0x0100" />
  </attribute>
  <attribute id="0x0201"> <!-- HIDParserVersion -->
    <uint16 value="0x0111" /> 
  </attribute>
  <attribute id="0x0202"> <!-- HIDDeviceSubclass -->
    <uint8 value="0x4c" />
  </attribute>
  <attribute id="0x0203"> <!-- HIDCountryCode -->
    <uint8 value="0x00" />
  </attribute>
  <attribute id="0x0204"> <!-- HIDVirtualCable -->
    <boolean value="true" />
  </attribute>
  <attribute id="0x0205"> <!-- HIDRecoonectInitiate -->
    <boolean value="true" />
  </attribute>
  <attribute id="0x0206"> <!-- HIDDescriptorList -->
    <sequence>
      <sequence>
        <uint8 value="0x22" />
        <text encoding="hex" value="05010906a101850175019508050719e029e715002501810295017508810395057501050819012905910295017503910395067508150026ff000507190029ff8100c0050c0901a1018503150025017501950b0a23020a21020ab10109b809b609cd09b509e209ea09e9093009B009B181029501750d8103c0" />
      </sequence>
    </sequence>
  </attribute>
  <attribute id="0x0207"> <!-- HIDLANGIDBaseList -->
    <sequence>
      <sequence>
        <uint16 value="0x0409" />
        <uint16 value="0x0100" />
      </sequence>
    </sequence>
  </attribute>
  <attribute id="0x0208"> <!-- HIDSDPDisable (Deprecated) -->
    <boolean value="true" />
  </attribute>
  <attribute id="0x0209"> <!-- HIDBatteryPower -->
    <boolean value="false" />
  </attribute>
  <attribute id="0x020a"> <!-- HIDRemoteWake -->
    <boolean value="true" />
  </attribute>
  <attribute id="0x020b"> <!-- HIDProfileVersion -->
    <uint16 value="0x1124" />
  </attribute>
  <attribute id="0x020c"> <!-- HIDSupervisionTimeout -->
    <uint16 value="0x0c80" />
  </attribute>
  <attribute id="0x020d"> <!-- HIDNormallyConnectable -->
    <boolean value="false" />
  </attribute>
  <attribute id="0x020e"> <!-- HIDBootDevice -->
    <boolean value="true" />
  </attribute>
  <attribute id="0x020f"> <!-- HIDSSRHostMaxLatency -->
    <uint16 value="0x0640" />
  </attribute>
  <attribute id="0x0210"> <!-- HIDSSRHostMinTimeout -->
    <uint16 value="0x0320" />
  </attribute>
</record>
"""
