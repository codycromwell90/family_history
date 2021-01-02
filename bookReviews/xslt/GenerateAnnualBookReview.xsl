<?xml version="1.0" encoding="UTF-8"?>
<!-- Generate Text File of book reviews for a given year. -->
<!-- Remeber to include $year argument when running! -->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:d="http://docbook.org/ns/docbook"
    exclude-result-prefixes="xs"
    version="2.0">
    
    <xsl:output method="text" indent="no"/>
    <xsl:param name="year"/>
    
    
    <xsl:template match="/">
        <!-- Heading, include grade scale -->
        <xsl:value-of select="$year"/><xsl:text> Reviews</xsl:text><xsl:text>&#10;</xsl:text>
        <xsl:text>&#10;</xsl:text>
        <xsl:value-of select="/d:book/d:info/d:abstract/d:formalpara/d:title"/><xsl:text>&#10;</xsl:text>
        <xsl:for-each select="/d:book/d:info/d:abstract/d:formalpara/d:para/d:simplelist/d:member">
            <xsl:text>&#009;</xsl:text><xsl:value-of select="normalize-space(.)"/><xsl:text>&#10;</xsl:text>
        </xsl:for-each>
        <xsl:text>&#10;</xsl:text>
        <xsl:text>&#10;</xsl:text>
        
        <!-- Miscellaneous comments -->
        <xsl:for-each select="/d:book/d:chapter[child::d:title[.=$year]]/d:simplesect[@label[.='note']]">
            <xsl:value-of select="./d:title/normalize-space(.)"/><xsl:text>&#10;</xsl:text>
            <xsl:value-of select="./d:para/normalize-space(.)"/><xsl:text>&#10;</xsl:text>
            <xsl:text>&#10;</xsl:text>
        </xsl:for-each>
        
        <!-- Book Reviews -->
        <xsl:for-each select="/d:book/d:chapter[child::d:title[.=$year]]/d:simplesect[@label[.='review']]">
            <xsl:text>Title: </xsl:text><xsl:value-of select="./d:title/d:emphasis/normalize-space(.)"/><xsl:text>&#10;</xsl:text>     
            <xsl:value-of select="./d:simplelist/d:member[1]/normalize-space(.)"/><xsl:text>&#10;</xsl:text>
            <xsl:value-of select="./d:simplelist/d:member[2]/normalize-space(.)"/><xsl:text>&#10;</xsl:text>
            <xsl:value-of select="./d:simplelist/d:member[3]/normalize-space(.)"/><xsl:text>&#10;</xsl:text>
            <xsl:text>&#009;</xsl:text><xsl:value-of select="./d:para/normalize-space(.)"/><xsl:text>&#10;</xsl:text>
            <xsl:text>&#10;</xsl:text>
        </xsl:for-each>
               
        <!-- Book of the year section -->
        <xsl:text>&#10;</xsl:text>
        <xsl:value-of select="/d:book/d:chapter[child::d:title[.=$year]]/d:simplesect[@label[.='bookOfTheYear']]/d:title"/><xsl:text>&#10;</xsl:text>
        <xsl:value-of select="/d:book/d:chapter[child::d:title[.=$year]]/d:simplesect[@label[.='bookOfTheYear']]/d:para/normalize-space(.)"/>
        
    </xsl:template>
      
</xsl:stylesheet>