import QtQuick 2.12
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.5

ApplicationWindow{
  visible: true
  width: 1000
  height: 600
  title: "Google Calendar"

  GridLayout {
      id : grid
      anchors.fill: parent
      rows    : 12
      columns : 12
      columnSpacing: 0
      rowSpacing: 0

      property double colMulti : grid.width / grid.columns
      property double rowMulti : grid.height / grid.rows

      function prefWidth(item){
          return colMulti * item.Layout.columnSpan
      } // Dopočet šířky
      function prefHeight(item){
          return rowMulti * item.Layout.rowSpan
      } // Dopočet výšky

      Rectangle {
          color : 'whitesmoke'
          Layout.rowSpan   : 12
          Layout.columnSpan: 8
          Layout.preferredWidth  : grid.prefWidth(this)
          Layout.preferredHeight : grid.prefHeight(this)

      }

      Rectangle {
          id : greenRect
          color : '#3498eb'
          Layout.rowSpan : 12
          Layout.columnSpan : 4
          Layout.preferredWidth  : grid.prefWidth(this)
          Layout.preferredHeight : grid.prefHeight(this)
      }

  }


}
