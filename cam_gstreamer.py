import gi

gi.require_version('Gst', '1.0')

from gi.repository import Gst



Gst.init(None)



pipeline = Gst.Pipeline()



src = Gst.ElementFactory.make('v4l2src', 'camera-source')

src.set_property('device', '/dev/video0')



sink = Gst.ElementFactory.make('ximagesink', 'display')



pipeline.add(src)

pipeline.add(sink)



src.link(sink)



pipeline.set_state(Gst.State.PLAYING)



bus = pipeline.get_bus()



msg = bus.timed_pop_filtered(

    Gst.CLOCK_TIME_NONE,

    Gst.MessageType.ERROR | Gst.MessageType.EOS

)


pipeline.set_state(Gst.State.NULL)
