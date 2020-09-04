<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:fo='http://www.w3.org/1999/XSL/Format'
    exclude-result-prefixes="xs"
    version="2.0">
    <xsl:import href="../../../../Program Files/Oxygen XML Editor 22/frameworks/docbook/xsl/fo/docbook.xsl"/>
    <xsl:import href="krush-titlepage.xsl"/>
       
    <xsl:param name="generate.toc" select="'book toc'"/>
    <xsl:param name="body.start.indent">1pc</xsl:param>

    
    <!--<xsl:template match="processing-instruction('hard-pagebreak')">
        <fo:block break-after='page'/>
    </xsl:template>-->
    
</xsl:stylesheet>