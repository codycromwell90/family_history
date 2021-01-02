<s:schema xmlns:s="http://purl.oclc.org/dsdl/schematron" 
            xmlns:db="http://docbook.org/ns/docbook" 
            xmlns:rng="http://relaxng.org/ns/structure/1.0">
    <s:ns prefix="db" uri="http://docbook.org/ns/docbook"/>
    <s:ns prefix="xlink" uri="http://www.w3.org/1999/xlink"/>
    
    <!-- pattern to verify @label in review, note,  -->
    <s:pattern>
        <s:title>Review Section Structure</s:title>
        <s:rule context="db:simplesect[@label='review']">
            <s:assert test="db:title">Section missing title.</s:assert>
            <s:assert test="db:simplelist">Section missing list</s:assert>
        </s:rule>
        <s:rule context="db:simplesect[@label='review']/db:simplelist">
            <s:assert test="count(db:member) = 4">Section simplelist must have 4 member elements.</s:assert>
            <s:assert test="db:member[1]/db:emphasis/text() = 'Author: '">member[1]/emphasis must be 'Author: '</s:assert>
            <s:assert test="db:member[2]/db:emphasis/text() = 'Date: '">member[2]/emphasis must be 'Date: '</s:assert>
            <s:assert test="db:member[3]/db:emphasis/text() = 'Grade: '">member[3]/emphasis must be 'Grade: '</s:assert>
        </s:rule>
    </s:pattern>
    <s:pattern>
        <s:title>Review Section Content</s:title>
        <s:rule context="db:chapter/db:simplesect[@label='review']/db:title">
            <s:assert test="db:emphasis[@role='underline']">Title missing underline</s:assert>
            <s:assert test="db:emphasis != 'Cat in the Hat'">Title is Cat in the Hat.</s:assert>
           <!-- <s:assert test="db:simplelist">Section missing list</s:assert>-->
        </s:rule>
        <s:rule context="db:chapter/db:simplesect[@label='review']/db:simplelist">
            <s:assert test="normalize-space(db:member[1]/text()) != 'Dr. Seuss'">Author is Dr. Seuss</s:assert>
            <s:assert test="normalize-space(db:member[2]/text()) != 'not finished'">Date is not finished</s:assert>
            <s:assert test="db:member[3]/text()='0' or db:member[3]/text()='1' or db:member[3]/text()='2' or db:member[3]/text()='3'
                or db:member[3]/text()='4' or db:member[3]/text()='5'">
                Grade must be 0, 1, 2, 3, 4, or 5</s:assert>
        </s:rule>
    </s:pattern>
    <s:pattern>
        <s:title>Review db:simplesect Structure</s:title>
        <s:rule context="db:simplesect">
            <s:assert test="./@label">simplesect missing label attribute</s:assert>
            <s:assert test="./@label[.='review'] | ./@label[.='bookOfTheYear'] | ./@label[.='note']">
                simplesect label must be 'review', 'bookOfTheYear' or 'note'</s:assert>
        </s:rule>
    </s:pattern>

</s:schema>