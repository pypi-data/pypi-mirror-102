define([
    'jquery'
    , 'nbextensions/visualpython/src/common/vpCommon'
    , 'nbextensions/visualpython/src/common/constant'
    , 'nbextensions/visualpython/src/common/StringBuilder'
    , 'nbextensions/visualpython/src/container/vpContainer'

    , '../constData.js'

    
], function ( $, vpCommon, vpConst, sb, vpContainer, 
              constData) {

    const { 
        STR_CLICK

        , VP_ID_PREFIX
        , VP_CLASS_PREFIX

        , VP_ID_APIBLOCK_MENU_BOX 
        , VP_ID_APIBLOCK_MENU_DELETE

        , VP_CLASS_APIBLOCK_BOARD
        , VP_CLASS_APIBLOCK_MENU_BOX
        , VP_CLASS_APIBLOCK_MENU_ITEM
    } = constData;

    var BlockMenu = function(blockContainer) {
        this.blockContainer = blockContainer;
        this.thisDom = '';
        this.block = undefined;

        this.position = {
            left: 0,
            top: 0
        }

        this.render();
        this.bindEvent();
    }

    /** render */
    BlockMenu.prototype.render = function() {
        var sbBlockMenu = new sb.StringBuilder();
        sbBlockMenu.appendFormatLine('<div id="{0}"  style="{1}" class="{2}">'
                                    , VP_ID_APIBLOCK_MENU_BOX, 'display: none; position: fixed;', VP_CLASS_APIBLOCK_MENU_BOX);
        // delete button
        sbBlockMenu.appendFormatLine('<div id="{0}" class="{1}">{2}</div>'
                                    , VP_ID_APIBLOCK_MENU_DELETE, VP_CLASS_APIBLOCK_MENU_ITEM, 'Delete');
        sbBlockMenu.appendLine('</div>');

        this.thisDom = $(sbBlockMenu.toString());

        // append on board body
        $(vpCommon.wrapSelector(VP_CLASS_PREFIX + VP_CLASS_APIBLOCK_BOARD)).append(this.thisDom);
    }

    BlockMenu.prototype.wrapSelector = function(query) {
        return vpCommon.wrapSelector(VP_ID_PREFIX + VP_ID_APIBLOCK_MENU_BOX + ' ' + query);
    }

    BlockMenu.prototype.show = function(block, left, top) {
        this.block = block;
        this.position = {
            left: left,
            top: top
        }
        this.thisDom.css(this.position)
        this.thisDom.show();
    }

    BlockMenu.prototype.close = function() {
        this.block = undefined;
        this.thisDom.hide();
    }

    BlockMenu.prototype.bindEvent = function() {
        var that = this;
        /** delete block */
        $(document).off(STR_CLICK);
        $(document).on(STR_CLICK, this.wrapSelector(VP_ID_PREFIX + VP_ID_APIBLOCK_MENU_DELETE), function() {
            that.block.deleteBlock_childBlockList();
            that.blockContainer.resetOptionPage();
            that.blockContainer.reRenderAllBlock_asc();
            that.close();
        });
    }

    return BlockMenu;

});