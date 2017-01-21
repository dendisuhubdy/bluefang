# -*- coding: utf-8 -*-

HID_PROFILE = """
<?xml version="1.0" encoding="UTF-8" ?>

<record>
	<attribute id="0x0001">
		<sequence>
			<uuid value="0x1124" />
		</sequence>
	</attribute>
	<attribute id="0x0004">
		<sequence>
			<sequence>
				<uuid value="0x0100" />
				<uint16 value="0x0011" />
			</sequence>
			<sequence>
				<uuid value="0x0011" />
			</sequence>
		</sequence>
	</attribute>
	<attribute id="0x0005">
		<sequence>
			<uuid value="0x1002" />
		</sequence>
	</attribute>
	<attribute id="0x0006">
		<sequence>
			<uint16 value="0x656e" />
			<uint16 value="0x006a" />
			<uint16 value="0x0100" />
		</sequence>
	</attribute>
	<attribute id="0x0009">
		<sequence>
			<sequence>
				<uuid value="0x1124" />
				<uint16 value="0x0100" />
			</sequence>
		</sequence>
	</attribute>
	<attribute id="0x000d">
		<sequence>
			<sequence>
				<sequence>
					<uuid value="0x0100" />
					<uint16 value="0x0013" />
				</sequence>
				<sequence>
					<uuid value="0x0011" />
				</sequence>
			</sequence>
		</sequence>
	</attribute>
	<attribute id="0x0100">
		<text value="Raspberry Pi Virtual Keyboard" />
	</attribute>
	<attribute id="0x0101">
		<text value="USB > BT Keyboard" />
	</attribute>
	<attribute id="0x0102">
		<text value="Raspberry Pi" />
	</attribute>
	<attribute id="0x0200">
		<uint16 value="0x0100" />
	</attribute>
	<attribute id="0x0201">
		<uint16 value="0x0111" />
	</attribute>
	<attribute id="0x0202">
		<uint8 value="0x40" />
	</attribute>
	<attribute id="0x0203">
		<uint8 value="0x00" />
	</attribute>
	<attribute id="0x0204">
		<boolean value="true" />
	</attribute>
	<attribute id="0x0205">
		<boolean value="true" />
	</attribute>
	<attribute id="0x0206">
		<sequence>
			<sequence>
				<uint8 value="0x22" />
				<text encoding="hex" value="05010906a101850175019508050719e029e715002501810295017508810395057501050819012905910295017503910395067508150026ff000507190029ff8100c0050c0901a1018503150025017501950b0a23020a21020ab10109b809b609cd09b509e209ea09e9093081029501750d8103c0" />
			</sequence>
		</sequence>
	</attribute>
	<attribute id="0x0207">
		<sequence>
			<sequence>
				<uint16 value="0x0409" />
				<uint16 value="0x0100" />
			</sequence>
		</sequence>
	</attribute>
	<attribute id="0x020b">
		<uint16 value="0x0100" />
	</attribute>
	<attribute id="0x020c">
		<uint16 value="0x0c80" />
	</attribute>
	<attribute id="0x020d">
		<boolean value="false" />
	</attribute>
	<attribute id="0x020e">
		<boolean value="true" />
	</attribute>
	<attribute id="0x020f">
		<uint16 value="0x0640" />
	</attribute>
	<attribute id="0x0210">
		<uint16 value="0x0320" />
	</attribute>
</record>
"""