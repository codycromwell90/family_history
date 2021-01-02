<?xml version="1.0" encoding="UTF-8"?>
<!-- Restructure book reviews so they produce good PDF. -->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:d="http://docbook.org/ns/docbook"
    exclude-result-prefixes="xs"
    version="2.0">

        <xsl:output method="xml" indent="no"/>
            
     <!-- Identity template -->  
    <xsl:template match="node() | @*">
            <xsl:copy>
                <xsl:apply-templates select="node() | @*"/>              
            </xsl:copy>
    </xsl:template>
    
    <!-- TODO - bug fix - drops @label='review' from output -->    
    <xsl:template match="d:chapter/d:simplesect[@label='review']">
        <xsl:copy><xsl:copy-of select="./d:title"></xsl:copy-of>
        <xsl:apply-templates select = "d:simplelist"></xsl:apply-templates>
        <xsl:apply-templates select="./d:simplelist/d:member[4]/d:annotation"/></xsl:copy>       
    </xsl:template>
    
    <xsl:template match="d:simplelist">     
        <xsl:copy>
            <xsl:copy-of select="./d:member[1]"></xsl:copy-of>
            <xsl:copy-of select="./d:member[2]"></xsl:copy-of>
            <xsl:copy-of select="./d:member[3]"></xsl:copy-of>
            <d:member><d:emphasis role="italic">Comments: </d:emphasis></d:member>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="d:simplelist/d:member[1]">
        <xsl:copy-of select="."></xsl:copy-of>
    </xsl:template>
    <xsl:template match="d:simplelist/d:member[2]">
        <xsl:copy-of select="."></xsl:copy-of>
    </xsl:template>
    <xsl:template match="d:simplelist/d:member[3]">
        <xsl:copy-of select="."></xsl:copy-of>
    </xsl:template>
    
    <xsl:template match="d:member[4]/d:annotation">
        <xsl:copy-of select="d:para"/>
    </xsl:template>
        
        
</xsl:stylesheet>