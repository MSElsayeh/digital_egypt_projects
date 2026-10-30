rule SSH_One {
        meta:
                Description = "Detects the presence of SSH-One malware."
        strings:
                $calloutDomain = "darkl0rd.com"
                $name = "SSH-One"
		$altName = "SSH-t"
        condition:
                any of them

}