import QtQuick 2.12
import QtQuick.Controls 2.5
import QtQuick.Controls 1.4 as Old
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

          Rectangle {
              id : header
              color : '#e3e3e3'
              width: parent.width
              height: 36

              Text {
                  anchors.left: parent.left
                  id: dateText
                  font.family: "Helvetica"
                  font.pointSize: 11
                  text: qsTr("")
              }

              Text {
                  anchors.right: parent.right
                  id: emailText
                  font.family: "Helvetica"
                  font.pointSize: 11
                  text: qsTr("")
              }
            }
            Component.onCompleted: {
              calendarConn.loadCredentials('')
              calendarConn.loadDate('')
            }
      }

      Rectangle {
          color : '#e3e3e3'
          Layout.rowSpan : 6
          Layout.columnSpan : 4
          Layout.preferredWidth  : grid.prefWidth(this)
          Layout.preferredHeight : grid.prefHeight(this)

          Old.Calendar {
              anchors.top: parent.top
              id: calendar
              width: parent.width
              height: 300

              onClicked: {
                calendarConn.printDate(date)
              }
          }
      }

      Rectangle {
          color : '#e3e3e3'
          Layout.rowSpan : 6
          Layout.columnSpan : 4
          Layout.preferredWidth  : grid.prefWidth(this)
          Layout.preferredHeight : grid.prefHeight(this)
          /*
          Button {
                  text: "Load Calendar"
                  width: parent.width
                  height: 40
                  background: Rectangle {
                      color: "#329ef0"
                  }
          }*/
      }
      Connections {
          target: calendarConn
          onPrintedDate: {
             dateText.text = "My events (" + printDate + ")"
          }
          onLoadedCredentials: {
            emailText.text = "Login as: " + loadedCredentials
          }
          onLoadedDate: {
            dateText.text = "My events (" + loadedDate + ")"
          }
      }
  }


}
