==================================
Data Acquistion and Authentication
==================================

There are multiple possible pathways to specify what data should be analyzed.
There are two broad categories of data that can be analyzed: a noise realization can be generated
or data from a frame file can be analyzed.

Noise simulation
----------------

For simulated data, the user should specify either the :code:`gaussian-noise` or :code:`zero-noise`
arguments.
In the former case, the data will be generated from a Gaussian distribution with the
specified PSDs (see below).
The specific noise realization can be controlled using the :code:`generation-seed` option.
For the latter, the data are assumed to contain no noise, while this is a valid realization
of the noise, it is not representative of typical noise.
For this case, the PSDs to be used can also be specified, although they don't influence the data.

Frame reading
-------------

When working with real data or more realistically simulated data, the data are read from frame files.
These can be in any format that can be read using :code:`gwpy.timeseries.TimeSeries.read`.
There are four methods that can be used to read data from frame files that proceed in the following order:

- queried from the gravitational-wave open science center (GWOSC), to use this method, the :code:`channel-dict`
  option should be set to, e.g., :code:`{"H1": "GWOSC"}`. This is the recommended method for most analyses of
  real data.
- explicitly passed using the `data-dict` option, in this case the data are read using
  :code:`gwpy.timeseries.TimeSeries.read` and the :code:`channel-dict` option should match a channel contained
  in the frame file.
- found using :code:`gwdatafind.find_urls` when :code:`bilby_pipe` is run. This method uses the
  :code:`channel-dict`, :code:`frame-type-dict`, :code:`data-find-url`, and :code:`data-find-urltype` options.
  Unless the channel being used is non-standard, e.g., contains glitch-subtracted data, the
  :code:`frame-type-dict`, :code:`data-find-url`, and :code:`data-find-urltype` can be usually left as their
  default values. When using this method, the :code:`transfer-files` option should be set to :code:`True` to
  make sure frames are properly copied to the working directory by :code:`HTCondor`.
- using :code:`gwpy.timeseries.TimeSeries.get` during the data generation job. This method uses the
  :code:`channel-dict` option and is the legacy method for finding data. If data reading from the above
  methods fails this will be used as the fallback option. It is not recommended to use this method unless
  the data are not available using the other methods. 

.. note::

   The :code:`gaussian-noise` and :code:`zero-noise` options supersede any option to read data from frame files.

PSD reading/generation
----------------------

In addition to the data containing the signal, the data options also determine how the noise PSDs are
specified.
When using the :code:`gaussian-noise` or :code:`zero-noise` options, the PSDs are either specified using the
:code:`psd-dict` option or using the default PSD for each specified detector.
When analysing time-domain data from frame files, the PSDs can be specified using the :code:`psd-dict` option,
or generated from data before the analysis segment read in the same way as above.
If a PSD file is specified through the :code:`psd-dict` for any interferometer it must be specified for all
interferometers.
To avoid forgetting to specify the PSD in one detector, if the default fallback option is desired for one
detector, the :code:`psd-dict` option can be set to :code:`None`, e.g., if
:code:`psd-dict={'H1': '/PATH/TO/PSD/filename.txt', 'L1': None}` is passed, :code:`/PATH/TO/PSD/filename.txt`
will be used for LIGO Hanford and the fallback method will be used for LIGO Livingston.

Authentication
--------------

Data finding is done using the :code:`scitokens` method.
We recommend that users consult `this page <https://computing.docs.ligo.org/guide/auth/scitokens/>`_ for
additional instructions.
In order to read proprietary frame files, the user must have a valid scitoken for the detector the
data comes from.
The first time submitting a job via `HTCondor` using scitoken authentication, the user should run
:code:`condor_vault_storer -v "igwn"` and follow the prompts to configure the credentials.
After this, it should be sufficient to create a kerberos token using :code:`kinit`.
More fine grained control over the generated token can be done by defining the :code:`HTGETTOKENOPTS`
environment variable.
This is especially useful when using robot authentication using the :code:`--role` and :code:`--credkey`
options.

When do I need to authenticate?
-------------------------------

- If the data are being read from a proprietary frame file stored on e.g., :code:`CVMFS`.
- If another file (e.g., PSD, ROQ basis) being used is in a proprietary location.
- If data are queried using :code:`gwpy.timeseries.TimeSeries.get`.
